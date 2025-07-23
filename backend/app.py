from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from backend.llm_agent import get_sql_from_llm
from backend.query_engine import run_query
from backend.visualizer import generate_bar_chart
import os

app = FastAPI()

# Serve static files (HTML, CSS, JS)
app.mount("/static", StaticFiles(directory="backend/static"), name="static")

# Allow CORS for frontend JavaScript to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Serve index.html at root
@app.get("/", response_class=HTMLResponse)
def serve_home():
    return FileResponse("backend/static/index.html")

# Main API endpoint
@app.post("/ask")
async def ask_question(request: Request):
    body = await request.json()
    question = body.get("question", "")

    print(f"📥 Incoming question: {question}")  # Debug log

    sql = get_sql_from_llm(question)

    if not sql:
        print("❌ LLM did not return SQL.")
        return JSONResponse(status_code=400, content={
            "question": question,
            "sql": None,
            "result": {"error": "LLM did not return valid SQL. Please rephrase your question."},
            "chart": None
        })

    print(f"✅ Generated SQL: {sql}")

    # Run SQL query
    result = run_query(sql)
    print(f"📊 Query result: {result}")

    # Optional chart generation
    image_base64 = None
    if isinstance(result, list) and result and isinstance(result[0], dict):
        keys = list(result[0].keys())
        if len(keys) >= 2:
            image_base64 = generate_bar_chart(result, keys[0], keys[1], title=question)

    return JSONResponse(content={
        "question": question,
        "sql": sql,
        "result": result,
        "chart": image_base64
    })
