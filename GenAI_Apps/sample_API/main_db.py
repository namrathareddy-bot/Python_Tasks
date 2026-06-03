import os
import mysql.connector
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MySQL configurations
DB_HOST = os.environ.get("MYSQL_HOST", "localhost")
DB_USER = os.environ.get("MYSQL_USER", "root")
DB_PASSWORD = os.environ.get("MYSQL_PASSWORD", "admin")
DB_NAME = os.environ.get("MYSQL_DB", "library_db")
DB_PORT = os.environ.get("MYSQL_PORT", "3306")

app = FastAPI(
    title="Gemini Database Chat API",
    description="FastAPI application which queries a MySQL database using natural language and Gemini AI.",
    version="1.0.0"
)

class ChatRequest(BaseModel):
    question: str

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

@app.get("/", response_class=HTMLResponse)
async def serve_ui():
    index_path = os.path.join(os.path.dirname(__file__), "static", "index_db.html")
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    return HTMLResponse(content="<h3>Database UI is under construction. Please ensure static/index_db.html is built.</h3>")

@app.post("/api/chat-db")
async def chat_with_db(request: ChatRequest):
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="GEMINI_API_KEY environment variable is missing on the server.")

    # 1. Fetch schema dynamically
    schema = get_database_schema()
    if "Error" in schema:
        raise HTTPException(status_code=500, detail=f"Database connection error: {schema}")

    client = genai.Client(api_key=api_key)
    
    # 2. Ask Gemini for SQL query
    prompt_sql = f"""
You are a highly skilled SQL generation assistant.
Given the following MySQL database schema, write a valid MySQL query to answer the user's question.

---
DATABASE SCHEMA:
{schema}
---

USER QUESTION:
{request.question}

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
        raise HTTPException(status_code=500, detail=f"AI SQL generation error: {str(e)}")

    # 3. Execute the SQL query
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

    # 4. Ask Gemini for final natural language answer
    if error:
        prompt_ans = f"""
The user asked: "{request.question}"
We generated this SQL query to answer it:
{sql_query}

However, executing the SQL query returned this error:
{error}

Explain this database error to the user in a helpful, conversational, and simple way.
"""
    else:
        prompt_ans = f"""
The user asked: "{request.question}"
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
        raise HTTPException(status_code=500, detail=f"AI Answer generation error: {str(e)}")

    return JSONResponse(content={
        "question": request.question,
        "sql": sql_query,
        "results": results,
        "error": error,
        "response": answer
    })

# Mount static files
static_dir = os.path.join(os.path.dirname(__file__), "static")
if not os.path.exists(static_dir):
    os.makedirs(static_dir)

app.mount("/static", StaticFiles(directory=static_dir), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main_db:app", host="127.0.0.1", port=8000, reload=True)
