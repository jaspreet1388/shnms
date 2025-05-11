# app.py
from fastapi import FastAPI
import time, random
app = FastAPI()

@app.get("/health")
def health_check():
    delay = random.uniform(0.1, 1.0)
    time.sleep(delay)
    return {"status": "ok", "latency": delay}

