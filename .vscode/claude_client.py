client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[
        {
            "role" : "user",
            "content" : ""
        }
    ],
     output_config={
        "format": {
            "type": "json_schema",
            "schema": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "email": {"type": "string"},
                    "urgency": {"type": "string"},
                    "category": {"type": "string"},
                    "reasoning": {"type": "string"},
                    "draft_reply": {"type": "string"},
                },
                "required": ["name", "email", "urgency"]
                },
        }
    },
)
print(response.content[0].text)
