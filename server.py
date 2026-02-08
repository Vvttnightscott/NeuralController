from fastapi import FastAPI
import uvicorn
from pyngrok import ngrok
import nest_asyncio

# Fix loop issues
nest_asyncio.apply()

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Neural Link Established"}

@app.get("/activate")
def activate_brain():
    print("🔴 SIGNAL RECEIVED: Activating Neural Network...")
    return {"message": "Command Executed", "power": 100}

if __name__ == "__main__":
    # Kill old tunnels
    ngrok.kill()
    
    # Create a NEW tunnel
    tunnel = ngrok.connect(8005)
    public_url = tunnel.public_url
    
    # Print the URL so you can copy it
    print(f"\n🚀 COPY THIS URL: {public_url}\n")
    
    # Start the server
    uvicorn.run(app, port=8005)