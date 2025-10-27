# 🧠 Dynamic Quote Generator API

A FastAPI backend that fetches real quotes dynamically from the **ZenQuotes API**.

## 🚀 Features
- `/` → Welcome route  
- `/random` → Returns a random quote  
- `/today` → Returns today’s quote  
- `/quotes` → Returns 10 quotes  

## ⚙️ Tech Stack
- Python
- FastAPI
- Requests (for external API calls)

## ▶️ Run Locally
```bash
git clone https://github.com/<your-username>/dynamic_quote_api.git
cd dynamic_quote_api
pip install -r requirements.txt
uvicorn main:app --reload
