## entry point - starts polling loop

from whatsapp import start_browser, send_message, get_last_message
import time

page = start_browser()
last_seen = get_last_message(page)

while True:
    time.sleep(3)
    current = get_last_message(page)
    if current != last_seen:
        print(f"New message: {current}")
        last_seen = current
        send_message(page, current)