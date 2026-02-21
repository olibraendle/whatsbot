## loads .env, exposes settings 

from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ALLOWED_CHAT_IDS = os.getenv("ALLOWED_CHAT_IDS", "")


print(OPENAI_API_KEY)