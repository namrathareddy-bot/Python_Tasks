import os
import mysql.connector
from flask import Flask, render_template, request, jsonify
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# MySQL connection parameters from .env
DB_HOST = os.environ.get("MYSQL_HOST", "localhost")
DB_USER = os.environ.get("MYSQL_USER", "root")
DB_PASSWORD = os.environ.get("MYSQL_PASSWORD", "admin")
DB_NAME = os.environ.get("MYSQL_DB", "library_db")
DB_PORT = os.environ.get("MYSQL_PORT", "3306")

def get_db_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        port=int(DB_PORT)
    )

def get_database_schema():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES")
        tables = [t[0] for t in cursor.fetchall()]
        
        schema_desc = []
        schema_desc.append(f"Database Name: {DB_NAME}\n")
        
        for table in tables:
            schema_desc.append(f"Table: {table}")
            cursor.execute(f"DESCRIBE `{table}`")
            columns = cursor.fetchall()
            for col in columns:
                schema_desc.append(f"  - {col[0]} ({col[1]})")
            schema_desc.append("")
            
        conn.close()
        return "\n".join(schema_desc)
    except Exception as e:
        return f"Error retrieving schema: {str(e)}"

def clean_sql_query(raw_query: str) -> str:
    cleaned = raw_query.strip()
    if cleaned.startswith("```"):
        lines = cleaned.split("\n")
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        cleaned = "\n".join(lines).strip()
    if cleaned.lower().startswith("sql\n"):
        cleaned = cleaned[4:].strip()
    elif cleaned.lower().startswith("sql "):
        cleaned = cleaned[4:].strip()
    return cleaned

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/chat-db", methods=["POST"])
def chat_with_db():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return jsonify({"detail": "GEMINI_API_KEY environment variable is missing on the server."}), 500

    req_data = request.get_json() or {}
    question = req_data.get("question", "").strip()
    if not question:
        return jsonify({"detail": "Question cannot be empty."}), 400

    # 1. Dynamically read schema
    schema = get_database_schema()
    if "Error" in schema:
        return jsonify({"detail": f"Database connection error: {schema}"}), 500

    # Initialize Gemini Client
    client = genai.Client(api_key=api_key)

    # 2. Ask Gemini to generate SQL
    prompt_sql = f"""
You are a highly skilled SQL generation assistant.
Given the following MySQL database schema, write a valid MySQL query to answer the user's question.

---
DATABASE SCHEMA:
{schema}
---

USER QUESTION:
{question}

---
CRITICAL INSTRUCTIONS:
1. Output ONLY the raw SQL query.
2. Do not explain the SQL query.
3. Do not wrap the SQL query in markdown blocks, but if you do, only use standard SQL formatting.
4. Ensure the query works on MySQL (use backticks where appropriate).
5. Only generate SELECT queries. Do not perform INSERT, UPDATE, or DELETE.

Provide the SQL query now:
"""
    try:
        response_sql = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt_sql
        )
        sql_query = clean_sql_query(response_sql.text)
    except Exception as e:
        return jsonify({"detail": f"AI SQL generation error: {str(e)}"}), 500

    # 3. Execute query in MySQL
    results = None
    error = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql_query)
        results = cursor.fetchall()
        conn.close()
    except Exception as e:
        error = str(e)

    # 4. Ask Gemini to formulate natural response
    if error:
        prompt_ans = f"""
The user asked: "{question}"
We generated this SQL query to answer it:
{sql_query}

However, executing the SQL query returned this error:
{error}

Explain this database error to the user in a helpful, conversational, and simple way.
"""
    else:
        prompt_ans = f"""
The user asked: "{question}"
We generated this SQL query to answer it:
{sql_query}

Executing this query returned the following rows/data from the MySQL database:
{results}

Write a natural, helpful, friendly, and complete human response that answers the user's question using the retrieved database data. Do not show raw SQL code in your answer unless the user asked for it. Keep it concise.
"""
    try:
        response_ans = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt_ans
        )
        answer = response_ans.text
    except Exception as e:
        return jsonify({"detail": f"AI Answer generation error: {str(e)}"}), 500

    return jsonify({
        "question": question,
        "sql": sql_query,
        "results": results,
        "error": error,
        "response": answer
    })

if __name__ == "__main__":
    app.run(debug=True, port=5005)
