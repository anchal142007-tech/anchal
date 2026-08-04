import os
from dotenv import load_dotenv
from pathlib import Path
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")


client = Groq(api_key=my_api_key)

model_name = "llama-3.3-70b-versatile"

message_1 = {
    "role": "system",
    "content": "You are a brand name suggester who suggest name for a brand in one word.",
}


message_2 = {
    "role": "user",
    "content": "Suggest a brand name for my food stall."
}

messages = [message_1, message_2]

response = client.chat.completions.create(
    model=model_name,
    messages=messages,  
    temperature=0.7,
)


print(response.choices[0].message.content)  