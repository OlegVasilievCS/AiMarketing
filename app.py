import anthropic

client = anthropic.Anthropic()

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