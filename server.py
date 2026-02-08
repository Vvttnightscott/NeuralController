# Version 2.0 - Live on Render
import os
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Neural Link Established"}

@app.get("/activate")
def activate_brain():
    print("🔴 SIGNAL RECEIVED: Activating Neural Network...")
    return {"message": "Command Executed", "power": 100}

if __name__ == "__main__":
    # 👇 This checks if Render gave us a port. 
    # If yes, use it. If no (local laptop), use 8000.
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)