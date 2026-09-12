from fastapi import FastAPI, Header, HTTPException, Depends
app = FastAPI()
SECRET = "BANGLA_AI_01913_LOCK_2026"

def verify(x_api_key: str = Header(None)):
    if x_api_key != SECRET:
        raise HTTPException(status_code=403, detail="Locked")
    return True

@app.get("/")
def home():
    return {"status": "Bangla AI Locked & Running"}

@app.get("/trend/{id}")
def trend(id: str, ok=Depends(verify)):
    return {"trend": id, "locked": True}
