from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI()

client = OpenAI()

# 🧠 THE MEMORY BANK (This is what was missing!)
sensor_memory = {"is_lifting": False, "x": 0.0, "y": 0.0}

class Thought(BaseModel):
    prompt: str

class SensorData(BaseModel):
    is_lifting: bool
    x: float
    y: float

@app.get("/")
def read_root():
    return {"status": "Neural Link Active", "sensor_data": sensor_memory}

# 1. The Phone calls this to UPDATE status
@app.post("/sensor")
def update_sensor(data: SensorData):
    global sensor_memory
    sensor_memory = {"is_lifting": data.is_lifting, "x": data.x, "y": data.y}
    print(f"📡 RECEIVED: {sensor_memory}") 
    return {"status": "Updated"}

# 2. Unity calls this to READ status
@app.get("/sensor")
def get_sensor():
    return sensor_memory

@app.post("/ask")
def ask_brain(thought: Thought):
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": thought.prompt}
            ]
        )
        return {"answer": completion.choices[0].message.content}
    except Exception as e:
        return {"answer": f"Error: {str(e)}"}
