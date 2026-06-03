import os
import mysql.connector
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MySQL Connection Details from .env
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
    """
    Automatically inspects the MySQL database and constructs a string
    describing the schema (tables, columns, types) to pass to Gemini.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Get list of tables
        cursor.execute("SHOW TABLES")
        tables = [t[0] for t in cursor.fetchall()]
        
        schema_desc = []
        schema_desc.append(f"Database Name: {DB_NAME}\n")
        
        for table in tables:
            schema_desc.append(f"Table: {table}")
            cursor.execute(f"DESCRIBE `{table}`")
            columns = cursor.fetchall()
            for col in columns:
                # col[0] is field name, col[1] is type
                schema_desc.append(f"  - {col[0]} ({col[1]})")
            schema_desc.append("") # empty line
            
        conn.close()
        return "\n".join(schema_desc)
    except Exception as e:
        print(f"Error fetching database schema: {e}")
        return ""

def clean_sql_query(raw_query: str) -> str:
    """
    Cleans up any markdown formatting (like ```sql ... ```)
    that Gemini might output, returning only the raw SQL statement.
    """
    cleaned = raw_query.strip()
    if cleaned.startswith("```"):
        # Remove starting code block
        lines = cleaned.split("\n")
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        cleaned = "\n".join(lines).strip()
    # Remove prefixing 'sql' word if present
    if cleaned.lower().startswith("sql\n"):
        cleaned = cleaned[4:].strip()
    elif cleaned.lower().startswith("sql "):
        cleaned = cleaned[4:].strip()
    
    # Remove semicolon at end if it causes issues, but standard mysql allows it
    return cleaned

def ask_gemini_for_sql(client, schema: str, question: str) -> str:
    """
    Asks Gemini to write a MySQL query to answer the user's question,
    given the dynamic database schema.
    """
    prompt = f"""
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
3. Do not wrap the SQL query in markdown blocks unless requested, but if you do, only use standard SQL formatting.
4. Ensure the query works on MySQL (use standard MySQL syntax, e.g. backticks for table or column names if they match reserved keywords).
5. Only generate SELECT queries. Do not perform INSERT, UPDATE, or DELETE.

Provide the SQL query now:
"""
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )
    return clean_sql_query(response.text)

def run_sql_query(query: str):
    """
    Runs the generated SQL query in the MySQL database and returns the results.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True) # return rows as dicts for easier reading
        print(f"\n[Executing SQL]: {query}")
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        return results, None
    except Exception as e:
        return None, str(e)

def ask_gemini_for_answer(client, question: str, query: str, results, error: str) -> str:
    """
    Takes the SQL query results and formats a human-friendly natural language response.
    """
    if error:
        prompt = f"""
The user asked: "{question}"
We generated this SQL query to answer it:
{query}

However, executing the SQL query returned this error:
{error}

Explain this error to the user in a helpful, conversational, and simple way.
"""
    else:
        prompt = f"""
The user asked: "{question}"
We generated this SQL query to answer it:
{query}

Executing this query returned the following rows/data from the MySQL database:
{results}

Write a natural, helpful, friendly, and complete human response that answers the user's question using the retrieved database data. Do not show raw SQL code in your answer unless the user asked for it. Keep it concise.
"""
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )
    return response.text

def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable is not set.")
        return

    # Initialize Gemini Client
    client = genai.Client(api_key=api_key)

    print("--- Dynamic Database Schema Extraction ---")
    schema = get_database_schema()
    if not schema:
        print("Could not fetch schema. Make sure MySQL is running and credentials in .env are correct.")
        return
    print(schema)
    print("-" * 50)

    # Get user question
    question = input("\nAsk a question about the database (e.g. How many students are there?): ")
    if not question.strip():
        question = "How many students are there in the table?"
        print(f"Defaulting to: {question}")

    # Step 1: Generate SQL using Gemini
    sql_query = ask_gemini_for_sql(client, schema, question)
    
    # Step 2: Run SQL query
    results, error = run_sql_query(sql_query)
    
    # Step 3: Format natural language response using Gemini
    answer = ask_gemini_for_answer(client, question, sql_query, results, error)
    
    print("\n" + "="*50)
    print("AI RESPONSE:")
    print("="*50)
    print(answer)
    print("="*50 + "\n")

if __name__ == "__main__":
    main()
