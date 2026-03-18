import threading
from bot import run_bot

active_bots = {}

def start_bot(username):
    if username in active_bots:
        return

    thread = threading.Thread(target=run_bot, args=(username,))
    thread.daemon = True
    thread.start()

    active_bots[username] = thread
    print(f"Bot started for {username}")

def stop_bot(username):
    # Nota: TikTokLive no tiene stop limpio fácil
    if username in active_bots:
        del active_bots[username]
        print(f"Bot stopped for {username}")
