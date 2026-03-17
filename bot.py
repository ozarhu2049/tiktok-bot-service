# bot.py

from TikTokLive import TikTokLiveClient
from TikTokLive.events import GiftEvent, CommentEvent
import requests
import os

# CONFIG
STREAMER_USERNAME = "username_del_streamer"
API_URL = "https://iartizan.com/api/tiktok/event"
API_KEY = "TU_API_KEY"

client = TikTokLiveClient(unique_id=STREAMER_USERNAME)


def send_event(data):
    try:
        requests.post(API_URL, json=data, headers={
            "Authorization": f"Bearer {API_KEY}"
        })
    except Exception as e:
        print("Error enviando evento:", e)


# 🎁 DETECTAR GIFTS (DIAMANTES)
@client.on(GiftEvent)
async def on_gift(event: GiftEvent):
    username = event.user.unique_id
    gift_name = event.gift.name
    diamonds = event.gift.diamond_count * event.repeat_count

    print(f"{username} envió {gift_name} ({diamonds} diamonds)")

    send_event({
        "type": "gift",
        "username": username,
        "diamonds": diamonds
    })


# 💬 DETECTAR COMENTARIOS (!bid)
@client.on(CommentEvent)
async def on_comment(event: CommentEvent):
    comment = event.comment
    username = event.user.unique_id

    print(f"{username}: {comment}")

    if comment.startswith("!bid"):
        try:
            amount = int(comment.split(" ")[1])

            send_event({
                "type": "bid",
                "username": username,
                "amount": amount
            })

        except:
            pass


if __name__ == "__main__":
    print("Bot conectado...")
    client.run()