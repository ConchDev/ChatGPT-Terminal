import openai 
import dotenv
import os
import datetime

dotenv.load_dotenv()

openai.api_key = os.getenv("OPENAI_KEY")

messages = []

def create():
    resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    messages.append(resp["choices"][0]["message"])

    return resp["choices"][0]["message"]


while True:
    if not messages:
        messages.append({
            "role": "system", "content": "You are ChatGPT, a large language model "
            "trained by OpenAI. Answer as concisely as possible. Knowledge cutoff: "
             f"2021 Current date: {str(datetime.datetime.now()).split(' ')[0]}"
        })
        continue
    
    msg = input("You>> ")

    if msg.lower() == "bye":
        print("Goodbye!")
        exit()

    messages.append({
        "role": "user",
        "content": msg
    })

    ai_msg = create()

    print(f"{ai_msg['role'].capitalize()}>> {ai_msg['content']}")
