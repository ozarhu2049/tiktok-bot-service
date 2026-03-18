from TikTokLive import TikTokLiveClient
from TikTokLive.events import GiftEvent

def run_bot(username):

    client = TikTokLiveClient(unique_id=username)

    @client.on(GiftEvent)
    async def on_gift(event: GiftEvent):
        print(f"🎁 {event.user.unique_id} sent {event.gift.name}")

        diamonds = event.gift.diamond_count
        bidder = event.user.unique_id

        # Aquí conectas con tu SaaS
        send_bid_to_backend(username, bidder, diamonds)

    client.run()


def send_bid_to_backend(streamer, bidder, diamonds):
    import requests

    try:
        requests.post(
            "https://iartizan.com/api/bid",
            json={
                "streamer": streamer,
                "bidder": bidder,
                "amount": diamonds
            }
        )
    except Exception as e:
        print("Error sending bid:", e)
