# 💬 Chainlit + Gemini Chatbot

A simple conversational AI chatbot built with **Chainlit** and **Google Gemini 2.5 Flash**.

---

## 📦 Project Outline

* **Chainlit** handles the UI and chat interface.
* **Google Generative AI** (Gemini 2.5 Flash) powers the responses.
* **Conversation history** is stored in memory during the session.
* **OAuth callback** is set up (e.g., for GitHub login).
* **Environment variables** are used to securely load the API key.

---

## 🔧 Requirements

* Python 3.9+
* `chainlit`
* `google-generativeai`
* `python-dotenv`

---

## 🚀 Quick Start

1. Add your Gemini API key to a `.env` file.
2. Install dependencies.
3. Run the app with:

```bash
chainlit run main.py
```
