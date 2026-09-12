from fastapi import FastAPI, Header, HTTPException, Depends
import threading, time, requests

app = FastAPI()
SECRET = "BANGLA_AI_01913_LOCK_2026"

# Lifeline - Ajibon Active
def keep_alive():
    while True:
        time.sleep(300)
        try:
            requests.get("https://-bangla-ai-server.onrender.com/")
        except:
            pass

threading.Thread(target=keep_alive, daemon=True).start()

def verify(x_api_key: str = Header(None)):
    if x_api_key != SECRET:
        raise HTTPException(status_code=403, detail="Locked")
    return True

@app.get("/")
def home():
    return {"status": "Bangla AI Locked & Lifeline Active"}

@app.get("/trend/{id}")
def trend(id: str, ok=Depends(verify)):
    return {"trend": id, "locked": True, "lifeline": "active"}
