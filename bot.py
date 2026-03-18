from TikTokLive import TikTokLiveClient
from TikTokLive.events import GiftEvent

def run_bot(username):
    client = TikTokLiveClient(unique_id=username)

    @client.on(GiftEvent)
    async def on_gift(event: GiftEvent):
        print(f"🎁 {event.user.unique_id} sent {event.gift.name}")
        diamonds = event.gift.diamond_count

        send_to_backend(username, event.user.unique_id, diamonds)

    client.run()


def send_to_backend(streamer, user, amount):
    import requests
    requests.post("https://iartizan.com/api/bid", json={
        "streamer": streamer,
        "user": user,
        "amount": amount
    })
