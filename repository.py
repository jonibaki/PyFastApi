from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    price: float
    is_offer: Optional[bool] = None

@app.get("/")
async def home():
    return {"Data": "Test"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.post("/items")
async def create_item(item: Item):
    return {"item_name": item.name}

@app.post("/items/all")
async def create_item(item: Item):
    return {"item_name": item.name}