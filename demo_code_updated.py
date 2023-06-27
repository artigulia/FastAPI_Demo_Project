from fastapi import FastAPI
from fastapi import Path
from typing import Optional
from pydantic import BaseModel
from fastapi import Query


app = FastAPI()

class Item(BaseModel):
    name : str
    price : float
    brand : Optional[str] = None

class UpdateItem(BaseModel):
    name : Optional[str] = None
    price : Optional[float] = None
    brand : Optional[str] = None

@app.get("/")
async def home():
    return {"Data" : "Testing"}

@app.get("/about")
async def about():
    return {"Data" : "About"}

inventory = { }
@app.get("/get-item/{item_id}")
#Setting path description
def get_item(item_id : int = Path(description="This is the ID of the item")):
    return inventory[item_id]

@app.get("/get-by-name/{item_id}")
# multiple parameters to the function
def get_item(*, item_id : int, test : int, name: Optional[str] = None):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    return {"Data" : "Not found"}


# Request code. inheriting the Base class
# Passing item object to post
@app.post("/create-item/{item_id}")
def create_item(item_id : int, item : Item):
    if item_id in inventory:
        return {"Error" : "item ID already exists!"}
    inventory[item_id] = item
    return inventory[item_id]


@app.put("/update_item/{item_id}")
def update_item(item_id : int, item : UpdateItem):
    if item_id not in inventory:
        return {"Error" : "Item does not exists"}
    if item.name != None:
        inventory[item_id].name = item.name
    if item.price != None:
        inventory[item_id].price = item.price
    if item.brand != None:
        inventory[item_id].brand = item.brand
    return inventory[item_id]

@app.delete("/delete-item")
def delete_item(item_id : int = Query(..., description = "The ID of the item to delete")):
    if item_id not in inventory:
        return {"Error" : "ID does not exists"}
    del inventory[item_id]
    return{ "Success" : "Item deleted"}


