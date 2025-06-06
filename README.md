# 🍱 foodpanda-lifetime-spend

> A simple Python script to calculate your lifetime spending on [Foodpanda Pakistan](https://www.foodpanda.pk). Fetches your full order history using Foodpanda’s API and prints the total in PKR.

---

## 📌 What it does

- Sends an authenticated API request to Foodpanda
- Fetches all past orders (up to 500)
- Extracts `total_value` from each order
- Prints your lifetime spend in PKR (with thousands separator)

---

## 🧰 Requirements

- Python 3.7+
- [`requests`](https://pypi.org/project/requests/) library

Install it with:

```bash
pip install requests
