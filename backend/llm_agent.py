import requests

OLLAMA_API_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3"

def get_sql_from_llm(question: str) -> str:
    prompt = f"""
You are an expert SQL assistant.

Given a natural language question, generate a full valid SQL query for SQLite.
Only use the tables and columns below. DO NOT use parameter placeholders like '?'.

### Available tables and columns:
- total_sales(date, item_id, total_sales, total_units_ordered)
- eligibility(eligibility_datetime_utc, item_id, eligibility, message)
- ad_sales(date, item_id, ad_sales, impressions, ad_spend, clicks, units_sold)

Generate only SQL directly, without markdown or explanations or another words.

Question: {question}
SQL:
"""

    response = requests.post(
        OLLAMA_API_URL,
        json={
            "model": "phi3:mini-4k",
            "prompt": prompt,
            "stream": False
        }
    )

    if response.status_code == 200:
        try:
            sql = response.json().get("response", "").strip()
            if sql.startswith("```sql"):
                sql = sql.replace("```sql", "").replace("```", "").strip()
            return sql
        except Exception as e:
            print("❌ JSON parsing failed:", e)
            return None
    else:
        print("❌ Ollama API call failed with status:", response.status_code)
        return None
