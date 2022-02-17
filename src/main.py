from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


class User(BaseModel):
    name: str
    full_name: str
    age: int


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def updated_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@app.put("/user_create/{user_id}")
def add_user(user_id: int, user: User):
    return {"user_name": user.name, "user_id": user_id}
