from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI()

# 1. Initialize the OpenAI Brain
# It automatically looks for "OPENAI_API_KEY" in the environment
client = OpenAI()

class Thought(BaseModel):
    prompt: str

@app.get("/")
def read_root():
    return {"status": "Neural Link Active", "mode": "OpenAI GPT-4o-Mini"}

@app.post("/ask")
def ask_brain(thought: Thought):
    try:
        # 2. Ask ChatGPT
        # gpt-4o-mini is the new standard: Fast, Cheap, Smart.
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant for a Unity game."},
                {"role": "user", "content": thought.prompt}
            ]
        )
        
        # 3. Extract Answer
        answer_text = completion.choices[0].message.content
        return {"answer": answer_text}

    except Exception as e:
        # If your credit card fails or key is wrong, this tells us why
        return {"answer": f"Brain Freeze: {str(e)}"}

