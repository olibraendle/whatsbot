from openai import OpenAI
from config import OPENAI_API_KEY
from memory import get_history

client = OpenAI(api_key=OPENAI_API_KEY)


def get_reply(message):
    char= ""
    with open("openai_char_ex.txt", "r") as ai_char:
        char = ai_char.read()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": char}] + get_history()
        
    )
    return response.choices[0].message.content