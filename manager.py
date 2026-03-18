import threading
from bot import run_bot

bots = {}

def start_bot(username):
    if username in bots:
        return

    t = threading.Thread(target=run_bot, args=(username,))
    t.daemon = True
    t.start()

    bots[username] = t

def stop_bot(username):
    if username in bots:
        del bots[username]
