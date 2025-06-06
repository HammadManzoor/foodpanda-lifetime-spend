"""
Fetch Foodpanda order history, sum every `total_value`, and print the result in PKR.

Dependencies:
    pip install requests
"""

import requests
import sys

# --------------------------------------------------------------------------- #
# 1. CONFIGURATION – Replace with your actual bearer token                    #
# --------------------------------------------------------------------------- #
BEARER_TOKEN = "REPLACE_WITH_YOUR_ACTUAL_JWT_TOKEN"

API_URL = (
    "https://pk.fd-api.com/api/v5/orders/order_history"
    "?include=order_products,order_details&limit=500"
)
API_KEY = "vovo"

# --------------------------------------------------------------------------- #
# 2. CORE LOGIC                                                               #
# --------------------------------------------------------------------------- #
def fetch_order_history() -> dict:
    headers = {
        "x-fp-api-key": API_KEY,
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Accept": "application/json",
        "User-Agent": "sum_total_value/1.1",
    }

    resp = requests.get(API_URL, headers=headers, timeout=15)
    resp.raise_for_status()
    return resp.json()


def sum_total_value(payload: dict) -> float | int:
    try:
        items = payload["data"]["items"]
    except (TypeError, KeyError):
        print("Payload is missing expected path data.items")
        sys.exit(1)

    return sum(item.get("total_value", 0) for item in items)

# --------------------------------------------------------------------------- #
# 3. OUTPUT                                                                   #
# --------------------------------------------------------------------------- #
def show_total(total: float | int) -> None:
    formatted = f"{total:,.0f} PKR"
    print(f"Total value of all orders: {formatted}")

# --------------------------------------------------------------------------- #
# 4. MAIN                                                                     #
# --------------------------------------------------------------------------- #
def main() -> None:
    payload = fetch_order_history()
    total = sum_total_value(payload)
    show_total(total)


if __name__ == "__main__":
    main()
