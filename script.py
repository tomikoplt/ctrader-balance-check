import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

# TEMP: simulate balance (we'll replace this later)
balance = 1600   # change this to test

if balance > 1500:
    message = f"Balance alert: {balance} EUR"
else:
    message = f"Balance OK: {balance} EUR"

requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": message,
    },
)
