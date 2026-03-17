# worker.py

import redis
import json
import subprocess

r = redis.Redis(host='localhost', port=6379, db=0)

print("Worker escuchando...")

while True:
    _, job_data = r.brpop("bot_queue")
    job = json.loads(job_data)

    username = job["username"]

    print(f"Iniciando bot para {username}")

    subprocess.Popen([
        "python",
        "bot.py",
        username
    ])