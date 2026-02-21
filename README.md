# whatsbot

A WhatsApp bot that replies to messages using AI (OpenAI / Anthropic).
Built as a learning project to practice Python project structure.

## Stack
- **WhatsApp**: [Green API](https://green-api.com) (free tier, REST-based)
- **AI**: OpenAI or Anthropic
- **Memory**: JSON file (via Python's built-in `json` module)
- **Config**: `python-dotenv`

## Setup

1. Create a free account at [green-api.com](https://green-api.com)
2. Create an instance and scan the QR code with your phone
3. Copy your `instance_id` and `api_token`

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then fill in your values
python main.py
```

## Project Structure

```
whatsbot/
├── main.py        # entry point, polling loop
├── config.py      # loads .env settings
├── whatsapp.py    # send/receive via Green API
├── ai.py          # AI API wrapper
├── memory.py      # conversation history per chat
└── handler.py     # routing logic and commands
```

## Commands
- `!help` — show available commands
- `!reset` — clear conversation history for this chat

## .env variables

```
GREEN_API_INSTANCE_ID=your_instance_id
GREEN_API_TOKEN=your_token
OPENAI_API_KEY=your_openai_key
ALLOWED_CHAT_IDS=          # comma-separated, leave empty to allow all
```
