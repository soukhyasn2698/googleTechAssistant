# app/main.py
from fastapi import FastAPI

root_agent = None
app = FastAPI()

def get_agent():
    global root_agent
    if root_agent is None:
        from helper_agent.agent import root_agent as agent
        root_agent = agent
    return root_agent

@app.get("/")
async def health():
    return {"status": "healthy"}

@app.post("/chat")
async def chat(message: dict):
    user_message = message.get("message", "")
    agent = get_agent()
    response = agent.run(user_message)
    return {"response": response}