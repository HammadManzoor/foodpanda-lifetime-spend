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
```
## 🔑 Setup

#### 1. Get your Foodpanda token:
- Log into foodpanda.pk in your browser
- Open Developer Tools → Application tab
- Look under Cookies for the key access_token
- Copy the token string

#### 2. Edit the script:
- Open the script and paste your token in the placeholder

```bash
BEARER_TOKEN = "your-token-here"
```

## 🚀 Run
```bash
python foodpanda_total.py
```
> Sample Output
```bash
Total value of all orders: 45,900 PKR
```

## ⚠️ Disclaimer
> This tool is for personal use only. It uses your own Foodpanda token to make authorized API requests. Do not share your token or commit it to public repositories.
