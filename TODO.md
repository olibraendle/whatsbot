# TODO

## Day 1 — Setup & receive messages
- [ ] Install dependencies: `pip install playwright python-dotenv openai`
- [ ] Install the browser: `playwright install chromium`
- [ ] Create `.env.example` with empty variable names
- [ ] Create `.env` with your real values
- [ ] Create `requirements.txt`
- [ ] Implement `config.py` — load `.env` and expose settings as variables
- [ ] Implement `whatsapp.py` — launch browser, open web.whatsapp.com, wait for QR scan
- [ ] Save the browser session to `session/` so you don't re-scan every time
- [ ] Implement `main.py` — start the browser and print incoming messages to terminal
- [ ] Add `session/` to `.gitignore`
- [ ] Test: send yourself a message and see it printed in the terminal

## Day 2 — Send replies
- [ ] Add a send function to `whatsapp.py` — find the message input and type/submit
- [ ] In `main.py`, echo every received message back
- [ ] Test: send a message, confirm the bot replies

## Day 3 — AI integration
- [ ] Get an OpenAI API key (platform.openai.com) or Anthropic key
- [ ] Add the key to `.env`
- [ ] Implement `ai.py` — takes a message string, returns AI reply string
- [ ] Wire `ai.py` into the loop: receive → ai → send
- [ ] Test: have a basic conversation with the bot

## Day 4 — Conversation memory
- [ ] Create `memory.py` — stores message history per chat in a JSON file
- [ ] Implement `load(chat_id)` and `save(chat_id, messages)` functions
- [ ] Pass the last N messages as context when calling the AI
- [ ] Test: confirm the bot remembers what you said earlier

## Day 5 — Handler + commands
- [ ] Create `handler.py` — receives a message, decides what to do
- [ ] Move routing logic out of `main.py` into `handler.py`
- [ ] Implement `!help` command
- [ ] Implement `!reset` command — clears memory for that chat
- [ ] Test all commands

## Day 6 — Robustness
- [ ] Add allowed chat IDs filter (read from `.env`, ignore others if set)
- [ ] Add basic rate limiting — don't reply more than once every N seconds per chat
- [ ] Wrap calls in try/except so one error doesn't crash the bot
- [ ] Test: what happens when OpenAI is slow or returns an error?

## Day 7 — Cleanup
- [ ] Read through all files and clean up messy code
- [ ] Make sure every file has one clear job
- [ ] Update `README.md` if anything changed
- [ ] Do a final `git add . && git commit -m "final cleanup" && git push`
- [ ] Reflect: what would you do differently? What to learn next?
