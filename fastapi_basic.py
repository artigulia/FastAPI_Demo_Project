from fastapi import FastAPI
from enum import Enum
app = FastAPI()

food_items = {
    'indian': ["Samosa", "Dosa"],
    'american' : ["Hot Dog", "American Pie"],
    'italian' : ["Pizza", "Pasta"]
}
class AvailableCuisine(str, Enum):
    indian = "indian"
    american = "american"
    italian = "italian"

coupon_code = {
    1 : "10%",
    2:"20%",
    3:"30%"
}

@app.get("/hello/{name}")
async def hello(name):
    return f"Hey {name }, Welcome to the first program"

@app.get("/get_items/{cuisine}")
async def get_items(cuisine : AvailableCuisine):
    return food_items.get(cuisine)

@app.get("/get_coupon/{code}")
async def get_items(code: int):
    return {'discount_amount' : coupon_code.get(code)}


