from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# RUN THIS COMMAND: uvicorn app:app --reload --host 0.0.0.0 --port 8000
# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

f_name = "Jason"
l_name = "Lamb"
fav_foods = ["Pizza","Lasagna","Chicken"]
hobbies = ["Golfing","3D Printing","Games"]

@app.get("/")
async def hello_world():
    return {"message": "Hello, World!"}

@app.get("/about-me")
async def about_me():
    return {"first_name": f_name,
            "last_name": l_name,
            "favorite_foods": fav_foods,
            "hobbies": hobbies}