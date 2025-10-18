from fastapi import FastAPI, Body
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="Chat with My Cloud")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.get("/")
def health_check():
    return {"status": "ok", "message": "Chat with My Cloud running locally"}

@app.post("/ask")
def ask(payload: dict = Body(...)):
    question = payload.get("question")
    if not question:
        return {"error": "Missing 'question' field"}

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": question}]
    )

    answer = response.choices[0].message.content
    return {"answer": answer}
