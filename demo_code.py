from fastapi import FastAPI
from fastapi import Path
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    name : str
    price : float
    brand : Optional[str] = None


@app.get("/")
async def home():
    return {"Data" : "Testing"}

@app.get("/about")
async def about():
    return {"Data" : "About"}

inventory = {
    1 : {
        "name": "Milk",
        "Price": 3.99,
        "brand": "Regular"
    }
}
@app.get("/get-item/{item_id}")
#Setting path description
def get_item(item_id : int = Path(description="This is the ID of the item")):
    return inventory[item_id]

@app.get("/get-by-name/{item_id}")
# multiple parameters to the function
def get_item(*, item_id : int, test : int, name: Optional[str] = None):
    for item_id in inventory:
        if inventory[item_id]['name'] == name:
            return inventory[item_id]
    return {"Data" : "Not found"}

# Request code. inheriting the Base class
@app.post("/create-item/{item_id}")
def create_item(item_id : int, item : Item):
    if item_id in inventory:
        return {"Error" :"item ID already exists!"}
    inventory[item_id] = {"name" : item.name, "brand": item.brand, "price" : item.price }
    return inventory[item_id]




