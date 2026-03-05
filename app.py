import anthropic
from dotenv import load_dotenv
import os


load_dotenv()
key = os.getenv("cluade_api_key")

client = anthropic.Anthropic(api_key=key)

message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "Search for the top 5 cybersecurity threats facing Montreal law firms in 2026.",
        }
    ],
)
print(message.content)


