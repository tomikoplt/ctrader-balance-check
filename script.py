import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

balance = 1600

if balance > 1500:
    message = f"Balance alert: {balance} EUR"
else:
    message = f"Balance OK: {balance} EUR"

response = requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": message,
    },
)

print("STATUS:", response.status_code)
print("RESPONSE:", response.text)

response.raise_for_status()
