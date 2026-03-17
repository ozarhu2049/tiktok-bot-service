from fastapi import FastAPI, HTTPException
from manager import start_bot, stop_bot

app = FastAPI()

@app.get("/")
def home():
    return {"status": "ok"}

@app.post("/start-bot")
def api_start_bot(data: dict):
    username = data.get("username")

    if not username:
        raise HTTPException(status_code=400, detail="Username required")

    start_bot(username)

    return {"message": f"Bot started for {username}"}

@app.post("/stop-bot")
def api_stop_bot(data: dict):
    username = data.get("username")

    if not username:
        raise HTTPException(status_code=400, detail="Username required")

    stop_bot(username)

    return {"message": f"Bot stopped for {username}"}
