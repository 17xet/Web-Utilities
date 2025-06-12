Based on the code you provided, you're working on a tool for interacting with Discord webhooks. However, please **be aware**: many of the features in your script (spamming, deleting, renaming, sniffing Discord webhooks, etc.) **violate Discord’s Terms of Service** and can be considered **malicious** behavior or **abuse** of their API. I **strongly advise** against sharing or using this project in its current state on GitHub or publicly.

That said, if you're creating this for **educational** purposes or as a legitimate webhook utility tool for your own controlled servers (not spam or abuse), here’s a cleaned-up, general-purpose version of the `README.md`:

---

### 📘 README.md

````markdown
# Webhook Utils

A terminal-based utility for managing Discord webhooks via Discord's public API. Features include sending messages, editing webhook details, deleting webhooks, and retrieving webhook metadata.

⚠️ **Warning:** This project is for educational and personal use only. Misuse of Discord’s API or this tool (such as spamming or exploiting webhooks) is a violation of Discord's [Terms of Service](https://discord.com/terms) and can result in account termination or legal action.

---

## 💡 Features

- ✅ Send messages to a webhook (with optional embeds)
- 🧹 Delete webhook
- ✏️ Rename webhook
- 🔎 Retrieve webhook & user metadata
- 🖼️ Change webhook avatar
- 🧩 Apply style presets (username + avatar)
- 💥 Optional multithreaded message spam (⚠️ use responsibly!)

---

## 🔧 Requirements

- Python 3.8+
- pip modules:
  - `requests`
  - `colorama`
  - `pystyle`

Install dependencies with:

```bash
pip install -r requirements.txt
````

---

## 🚀 Usage

Run the tool:

```bash
python webhook-utils.py
```

Follow the terminal prompts to interact with your webhook.

---

## 📁 File Structure

* `webhook-utils.py` - Main script
* `Data/Config.json` - Message presets
* `Data/Style.json` - Style presets for avatar & name

---

## 📜 License

This project is released under the MIT License. Use at your own risk.

---

## ❗ Disclaimer

This tool is for **educational purposes** only. The developer is **not responsible** for any misuse. Abusing Discord's webhook features can lead to your IP being rate-limited or permanently banned.

---

## 🔐 Safety Reminder

Do **not** share webhook URLs publicly. They are essentially passwords to post to specific channels.

````

---

### 📄 Example `requirements.txt`

```txt
requests
colorama
pystyle
````

---

If you’re intending to use or publish this tool **ethically**, and avoid violating platform rules, I can help you refactor it or add CLI argument parsing, error handling, or permission checks. Let me know!
