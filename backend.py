from openai import OpenAI
from pydantic import BaseModel

import tools

SERVER_API_HOST = "http://172.25.112.1:1234/v1"

client = OpenAI(base_url = SERVER_API_HOST, api_key = "not-needed-XD")

class Command(BaseModel):
    command: str
    arguments: list[str]
    explainingArguments: str

class Instructions(BaseModel):
    description: str
    commands: list[Command]

tools = [
    {
        "type": "function",
        "function": {
            "name": "run_command",
            "description": "Runs the command with the given arguments in a bash shell",
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string",
                        "description": "The command to be run"
                    },
                    "args": {
                        "type": "list of strings",
                        "description": "List of arguments and flags to be run with the command"
                    }
                },
                "required": ["command", "args"]
            }
        }
    }
]

completion = client.chat.completions.create(
    model = "dolphin3.0-llama3.1-8b",
    messages = [
        {"role": "system", "content": "You are Dolphin, a helpful cybersecurity professional."},
        {"role": "user", "content": "Can you scan the local site 172.16.112.1 for vulnerabilities?"}
    ],
    temperature = 0.7,
    tools = tools,
)

print(completion.choices[0].message.tool_calls[0])
