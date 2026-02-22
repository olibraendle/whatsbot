## entry point - starts polling loop

from whatsapp import start_browser, send_message, get_last_message
from ai import get_reply
import time
from memory import add_message

page = start_browser()
last_seen = get_last_message(page)

while True:
    time.sleep(3)
    current = get_last_message(page)
    if current != last_seen:
        print(f"New message: {current}")
        last_seen = current
        add_message("user", current)
        reply = get_reply(current)
        add_message("assistant", reply)
        send_message(page, reply)
        last_seen = reply


