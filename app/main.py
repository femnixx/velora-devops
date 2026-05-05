from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import time, os

app = FastAPI(title="Velora API", version="1.0")
START = time.time()

class Item(BaseModel): 
    name: str
    price: float

items = {}

@app.get("/health")
def health():
    return { "status": "ok", "uptime_s": round(time.time() - START)}

@app.get("/items")
def list_items(): 
    return list(items.values())

@app.post("/items/{item_id}")
def create_item(item_id: str, item: Item):
    if item_id in items: 
        raise HTTPException(409, "Already exists")
    items[item_id] = {"id": item_id, **item.model_dump()}
    return items[item_id]

@app.get("/items/{item_id}")
def get_item(item_id: str):
    if item_id not in items:
        raise HTTPException(404, "Not found")
    return items[item_id]
