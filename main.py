from fastapi import FastAPI, HTTPException
from manager import start_bot, stop_bot

app = FastAPI()

@app.get("/")
def home():
    return {"status": "ok"}

@app.post("/start-bot")
def start(data: dict):
    username = data.get("username")
    if not username:
        raise HTTPException(status_code=400, detail="Username required")

    start_bot(username)
    return {"message": "Bot started"}

@app.post("/stop-bot")
def stop(data: dict):
    username = data.get("username")
    stop_bot(username)
    return {"message": "Bot stopped"}
