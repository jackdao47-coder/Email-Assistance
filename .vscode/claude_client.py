from pydantic import BaseModel
from anthropic import Anthropic
from typing import Literal
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(dotenv_path=Path(__file__).parent.parent / ".env")


client = Anthropic()

#input model
class EmailContent(BaseModel):
    subject: str
    body: str


email = EmailContent(
    subject="Group Meeting for Sprint 2",
    body="Hi Jack, Are you okay to join a meeting this Saturday?"
)

#output model
class EmailProperties(BaseModel):
    urgency: Literal["Urgent", "High", "Normal"]
    category: Literal["Job/Application", "Academic/University", "Team/GroupWork", "Meeting/Scheduling", "Newsletter/Spam"]
    reasoning: str
    draft_reply: str

def TriageEmail(subject: str, body: str):
    response = client.messages.create(
        model="claude-sonnet-4.6",
         max_tokens=1024,
        system= "You are an email sorting assitant. Sort the email into the respective classes and return JSON only that matches the provided schema",
        messages=[
            {
                "role": "user",
                "content": f"""Classify this email:
    Subject: {email.subject}

    Body:
    {email.body}
    """
            }
        ],

        output_config={
            "format": {
                "type": "json_schema",
                "schema": EmailProperties.model_json_schema()
            }
        }
    )   

    print(response.content[0].text)
    return response
