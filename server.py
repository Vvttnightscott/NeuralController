from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import google.generativeai as genai
import os

app = FastAPI()

# 👇 PASTE YOUR KEY HERE (Keep the quotes!)
GEMINI_KEY = "AIzaSyBBpChPX5Vz8c3PkmG6Oy873rxPNzAdaIg"

# Configure the Brain
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

class Thought(BaseModel):
    prompt: str

@app.get("/")
def read_root():
    return {"status": "Neural Link Active", "mode": "Oracle"}

@app.post("/ask")
async def ask_brain(thought: Thought):
    try:
        print(f"Thinking about: {thought.prompt}")
        
        # Ask Gemini
        response = model.generate_content(thought.prompt)
        
        return {
            "answer": response.text,
            "power_usage": "Low"
        }
    except Exception as e:
        print(f"Brain Freeze: {e}")
        raise HTTPException(status_code=500, detail=str(e))