from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import logging

import numpy as np
import weaviate
from weaviate.util import get_valid_uuid
from uuid import uuid4

from backend.queries import populate_query, get_prod_uuid, get_user_vector_and_clicks, searchbar_query

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


client = weaviate.Client("http://localhost:8080")
# start a new User session
data_properties = {"sessionNumber": 0}
user_id = get_valid_uuid(uuid4())
client.data_object.create(data_properties, "User", user_id)

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    random_vector = np.random.rand(512)
    data = populate_query(random_vector, client)
    context = {"request": request, "data": data}
    return templates.TemplateResponse("index.html", context=context)

@app.post("/image-clicked")
async def image_clicked(data: dict, request: Request):
    labelName = data.get("imagePath")
    print(labelName)
    query_labelName = labelName.replace("images/", "").replace(".jpg", "")
    prod_uuid = get_prod_uuid(query_labelName, client)
    _, user_clicks = get_user_vector_and_clicks(user_id, client)
    if labelName in user_clicks:
        client.data_object.reference.delete(
            from_uuid = user_id,
            from_property_name = "likedItem",
            to_uuid = prod_uuid
        )
    else:
        client.data_object.reference.add(
            from_uuid = user_id,
            from_property_name = "likedItem",
            to_uuid = prod_uuid
        )

    user_vector, user_clicks = get_user_vector_and_clicks(user_id, client)
    if len(user_vector) < 1:
        user_vector = np.random.rand(512,)

    data = populate_query(user_vector, client)
    return_dict = {
        "data": data,
        "user_clicks": user_clicks
    }
    return return_dict

@app.post("/text-search")
def text_search(data: dict, request: Request):
    text_query = data.get("searchQuery")
    _, user_clicks = get_user_vector_and_clicks(user_id, client)
    data = searchbar_query(text_query, user_id, user_clicks, client)
    return_dict = {
        "data": data,
        "user_clicks": user_clicks
    }
    # will need something with the user_clicks also
    return return_dict

@app.post("/basket-clicked")
async def basket_clicked(data: dict, request: Request):
    basket_id = data.get("basket")
    print(basket_id)
    # Do something with the basket ID, like updating the database or sending a message to a message queue
    image_dict = {
        "image1": "images/l/t/lt02.jpg",
        "image2": "images/l/t/lt03.jpg",
        "image3": "images/l/t/lt04.jpg",
        "image4": "images/l/t/lt05.jpg",
        "image5": "images/l/t/lt06.jpg",
        "image6": "images/l/t/lt01.jpg",
        "image7": "images/l/t/lt02.jpg",
        "image8": "images/l/t/lt03.jpg",
        "image9": "images/l/t/lt04.jpg",
    }
    return image_dict
    #return {"message": f"Received basket clicked event for basket {basket_id}"}