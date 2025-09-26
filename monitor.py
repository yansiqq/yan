import requests
import time

API_URL = "https://api.coindesk.com/v1/bpi/currentprice.json"

def get_btc_price():
    try:
        response = requests.get(API_URL)
        data = response.json()
        price = data["bpi"]["USD"]["rate"]
        print(f"💰 Current Bitcoin Price: ${price}")
    except Exception as e:
        print("Error fetching data:", e)

if __name__ == "__main__":
    while True:
        get_btc_price()
        time.sleep(10)
