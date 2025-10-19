from fastapi import FastAPI, Body
from openai import OpenAI
from dotenv import load_dotenv
from mangum import Mangum
import boto3, os, json

# Try loading .env only for local/dev
if os.getenv("AWS_EXECUTION_ENV") is None:
    # Only loads .env in local mode
    load_dotenv()
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
else:
    # Running in Lambda → load from Parameter Store
    ssm = boto3.client("ssm", region_name=os.getenv("AWS_REGION", "us-east-1"))
    param_name = os.getenv("OPENAI_API_KEY")
    response = ssm.get_parameter(Name=param_name, WithDecryption=True)
    OPENAI_API_KEY = response["Parameter"]["Value"]

# Other configs from environment
STAGE = os.getenv("STAGE", "local")
REGION = os.getenv("AWS_REGION", "us-east-1")

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

app = FastAPI(title="Chat with My Cloud")

@app.get("/")
def health_check():
    return {
        "status": "ok",
        "stage": STAGE,
        "region": REGION,
        "message": "Chat with My Cloud running"
    }

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

# Required for AWS Lambda
handler = Mangum(app)
