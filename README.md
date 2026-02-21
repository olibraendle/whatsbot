# whatsbot

A WhatsApp bot that replies to messages using AI (OpenAI / Anthropic).
Built as a learning project to practice Python project structure.

## Stack
- **WhatsApp**: Playwright (controls WhatsApp Web in a browser — no third party)
- **AI**: OpenAI or Anthropic
- **Memory**: JSON file (via Python's built-in `json` module)
- **Config**: `python-dotenv`

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
cp .env.example .env   # then fill in your values
python main.py         # scan the QR code on first run
```

On first run a browser window opens — scan the QR code with your phone.
The session is saved in `session/` so you only need to do this once.

## Project Structure

```
whatsbot/
├── main.py        # entry point, starts browser and polling loop
├── config.py      # loads .env settings
├── whatsapp.py    # browser automation (send/receive via Playwright)
├── ai.py          # AI API wrapper
├── memory.py      # conversation history per chat
├── handler.py     # routing logic and commands
└── session/       # saved browser session (never commit this)
```

## Commands
- `!help` — show available commands
- `!reset` — clear conversation history for this chat

## .env variables

```
OPENAI_API_KEY=your_openai_key
ALLOWED_CHAT_IDS=          # comma-separated, leave empty to allow all
```
