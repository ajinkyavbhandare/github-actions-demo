import asyncio

from fastapi import FastAPI

app = FastAPI()


# Simulated "Experimental" computation (e.g., your Ψ-dynamics)
def complex_math(n: int):
    # Mimics CPU-bound work
    result = 0
    for i in range(n):
        result += i**2
    return result


@app.get("/")
async def root():
    return {"message": "System Operational"}


@app.post("/compute")
async def compute_data(payload: dict):
    # Offload blocking code to a threadpool to avoid blocking the event loop
    n = payload.get("n", 1000)
    result = await asyncio.to_thread(complex_math, n)
    return {"result": result}
