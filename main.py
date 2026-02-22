## entry point - starts polling loop

from whatsapp import start_browser, send_message


page = start_browser()
send_message(page, "hello from the bot")

print("Whatsapp is ready")
