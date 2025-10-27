from fastapi import FastAPI
import requests, random, json
from fastapi.responses import JSONResponse, HTMLResponse

app = FastAPI(
    title="🌟 Dynamic Quote Generator API",
    description="Fetches live inspirational quotes from ZenQuotes.io API",
    version="1.1.1"
)

ZEN_API = "https://zenquotes.io/api"

# ==============================
# 🚀 Info Endpoint
# ==============================
@app.get("/", tags=["Info"])
def root():
    return {"message": "Welcome to the Dynamic Quote Generator API 🚀"}

# ==============================
# 🧠 Random Quote Endpoint
# ==============================
@app.get("/random", tags=["Quotes"])
def random_quote():
    """Return a random quote from ZenQuotes API."""
    response = requests.get(f"{ZEN_API}/random")
    data = response.json()
    pretty_data = {
        "status": "success",
        "data": {
            "quote": data[0]["q"],
            "author": data[0]["a"]
        }
    }
    return JSONResponse(
        content=json.loads(json.dumps(pretty_data, indent=4)),
        media_type="application/json"
    )

# ==============================
# 🌞 Today's Quote Endpoint
# ==============================
@app.get("/today", tags=["Quotes"])
def today_quote():
    """Return today's quote."""
    response = requests.get(f"{ZEN_API}/today")
    data = response.json()
    pretty_data = {
        "status": "success",
        "data": {
            "quote": data[0]["q"],
            "author": data[0]["a"]
        }
    }
    return JSONResponse(
        content=json.loads(json.dumps(pretty_data, indent=4)),
        media_type="application/json"
    )

# ==============================
# 🎲 Random Quote from Full List
# ==============================
@app.get("/quote", tags=["Quotes"])
def one_quote():
    """Return one random quote from the full quote list."""
    response = requests.get(f"{ZEN_API}/quotes")
    data = response.json()
    q = random.choice(data)
    pretty_data = {
        "status": "success",
        "data": {
            "quote": q["q"],
            "author": q["a"]
        }
    }
    return JSONResponse(
        content=json.loads(json.dumps(pretty_data, indent=4)),
        media_type="application/json"
    )

# ==============================
# 🌈 Pretty HTML Quote Page
# ==============================
@app.get("/pretty", tags=["Visual"])
def pretty_quote():
    """Return a styled HTML quote card."""
    response = requests.get(f"{ZEN_API}/random")
    data = response.json()[0]
    quote = data["q"]
    author = data["a"]

    html = f"""
    <html>
        <head>
            <title>🌟 Dynamic Quote</title>
            <style>
                body {{
                    background: #0d1117;
                    color: #e6edf3;
                    font-family: 'Inter', sans-serif;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    text-align: center;
                    padding: 0 20px;
                }}
                .quote {{
                    font-size: 1.8rem;
                    max-width: 600px;
                    margin-bottom: 1rem;
                    line-height: 1.5;
                }}
                .author {{
                    color: #58a6ff;
                    font-size: 1.2rem;
                }}
            </style>
        </head>
        <body>
            <div class="quote">“{quote}”</div>
            <div class="author">– {author}</div>
        </body>
    </html>
    """
    return HTMLResponse(content=html)
