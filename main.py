from fastapi import FastAPI
from pydantic import BaseModel
from helpers.agent_manager import process_user_message
from agents.greeting_agent import greeting_agent

app = FastAPI()

# Root welcome endpoint
@app.get("/")
def root():
    return {
        "message": "👋 Welcome to CareConnect API! Use the /chat endpoint to talk to the assistant."
    }

# Ping to wake up Render's cold start
@app.get("/wake")
def wake_backend():
    return {
        "status": "Backend is awake and ready!",
        "message": "Hi there! CareConnect is ready to chat with you. 💬"
    }

# Greeting on session start
@app.get("/greet")
def greet_user():
    response = greeting_agent()
    return {
        "agent": response["agent"],
        "message": response["response"]
    }

# Chat Message Schema
class ChatRequest(BaseModel):
    message: str

# Main chat endpoint
@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    result = process_user_message(request.message)
    return result