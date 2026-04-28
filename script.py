import requests

URL = "https://ct.ictrading.com/investor/gZtlVBIoWA?u=martin_oplt"

response = requests.get(URL)

print("STATUS:", response.status_code)
print(response.text[:2000])  # print first 2000 chars
