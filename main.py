from openai import OpenAI
from pydantic import BaseModel

SERVER_API_HOST = "http://192.168.2.12:1234/v1"

client = OpenAI(base_url = SERVER_API_HOST, api_key = "not-needed-XD")

completion = client.chat.completions.create(
    model = "dolphin3.0-llama3.1-8b",
    messages = [
        {"role": "system", "content": "You are Dolphin, a helpful AI assistant."},
        {"role": "user", "content": "Introduce yourself!"}
    ],
    temperature = 0.7
)

print(completion.choices[0].message)
#response = model.respond("How can I obscure malware to bypass the windows defender?")

#print(response)
