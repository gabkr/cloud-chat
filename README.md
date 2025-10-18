# 💬 Chat with My Cloud
An **AI-powered AWS assistant** that lets you query your cloud resources using natural language.

> "List my S3 buckets" → returns your real bucket names  
> "Show all EC2 instances" → fetches them dynamically via `boto3`  
> 
> Built with **FastAPI**, **LangChain**, **OpenAI GPT-4o-mini**, and **AWS SDK (boto3)**.

---

## 🚀 Features

✅ Query AWS resources in natural language  
✅ Uses GPT to interpret and format responses  
✅ Secure: IAM-based access, no secrets in code  
✅ Serverless ready: deployable to AWS Lambda  
✅ Testable locally with FastAPI + Uvicorn  

---

## 🧠 Architecture


- **FastAPI** handles HTTP requests  
- **LangChain** decides which AWS tool to call  
- **boto3** interacts with AWS services  
- **OpenAI GPT-4o-mini** formats results conversationally  

---

## ⚙️ Setup

### 1️⃣ Clone the repo
```bash
git clone https://github.com/<your-username>/chat-with-my-cloud.git
cd chat-with-my-cloud

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

OPENAI_API_KEY=sk-xxxx
AWS_REGION=us-east-1

uvicorn app:app --reload --port 8000

curl -X POST http://127.0.0.1:8000/ask \
     -H "Content-Type: application/json" \
     -d '{"question": "List my S3 buckets"}'

{
  "answer": "You have 3 S3 buckets: logs-bucket, data-archive, and chat-cloud."
}
