from fastapi import FastAPI
from pydantic import BaseModel
from claude_client import TriageEmail


class EmailContent(BaseModel):
    subject: str
    body: str
    

app = FastAPI()


@app.get("/health")
def root():
    return {"status": "ok"}

@app.post("/triage")
async def triage(email:EmailContent):
    response = TriageEmail(email.subject, email.body)
    return {
        response
    }