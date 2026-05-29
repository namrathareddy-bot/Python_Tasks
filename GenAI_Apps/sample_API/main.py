import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Gemini AI FastAPI",
    description="FastAPI service integrated with Google GenAI SDK",
    version="1.0.0"
)

# API Request Model
class GenerationRequest(BaseModel):
    question: str

# Serve the beautiful frontend
@app.get("/", response_class=HTMLResponse)
async def read_index():
    index_path = os.path.join(os.path.dirname(__file__), "static", "index.html")
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    return HTMLResponse(content="<h3>Static frontend file not found. Please ensure static/index.html is created.</h3>")

# Streaming API Endpoint
@app.post("/api/generate")
async def generate_ai_response(request: GenerationRequest):
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key or api_key == "your_gemini_api_key_here":
        raise HTTPException(
            status_code=400, 
            detail="GEMINI_API_KEY is not configured on the server. Please set it in the .env file."
        )

    # Initialize Gemini Client
    client = genai.Client(api_key=api_key)
    model = "gemini-3-flash-preview"

    # Streaming generator function
    def stream_generator():
        try:
            response_stream = client.models.generate_content_stream(
                model=model,
                contents=request.question
            )
            for chunk in response_stream:
                if chunk.text:
                    yield chunk.text
        except Exception as e:
            yield f"\n[Error: {str(e)}]"

    return StreamingResponse(stream_generator(), media_type="text/event-stream")

# Mount static files (for css/js)
static_dir = os.path.join(os.path.dirname(__file__), "static")
if not os.path.exists(static_dir):
    os.makedirs(static_dir)

app.mount("/static", StaticFiles(directory=static_dir), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
