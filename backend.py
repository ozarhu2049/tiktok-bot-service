# backend.py

from fastapi import FastAPI
import redis
import json

app = FastAPI()

r = redis.Redis(host='localhost', port=6379, db=0)

@app.post("/start-bot")
def start_bot(streamer_id: str, tiktok_username: str):

    job = {
        "streamer_id": streamer_id,
        "username": tiktok_username
    }

    r.lpush("bot_queue", json.dumps(job))

    return {"status": "queued"}