# 🪙 CryptoAgent

A conversational **AI agent** that fetches **real-time cryptocurrency and exchange data** using [Coinlore API](https://www.coinlore.com/cryptocurrency-data-api).
Built with **Agents API + Gemini**, type-safe models, and an interactive **Chainlit UI**.

---

## 🚀 Features

* 🔎 Fetch live prices, rank, market cap, and supply info for coins.
* 🏦 Get exchange-specific trading data (price, volume, base/quote).
* ⚡ Query multiple coins or exchanges in a single request.
* ✅ Type safety with `TypedDict` & `dataclasses`.
* 🎨 Integrated **Chainlit UI** for chat-based interaction.

---

## 🛠️ Tech Stack

* **Python 3.10+**
* **Agents API** (`agents`)
* **Gemini (via OpenAI-style client)**
* **Requests** for API calls
* **dotenv** for config
* **Chainlit** for UI

---

## 📌 Example Queries

> *"What is the price of BTC and ETH?"*
> *"Give me the trading volume of Binance exchange."*

CryptoAgent automatically calls the right tools (`get_coins` or `get_info`) and responds with fresh data.

---

## 📑 API Reference

* **Coins endpoint** → `https://api.coinlore.net/api/tickers/`
* **Exchange endpoint** → `https://api.coinlore.net/api/coin/markets/?id=90`

---
