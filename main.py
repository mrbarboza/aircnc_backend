from fastapi import FastAPI, Response
from pydantic import BaseModel
from pymongo import MongoClient

# Config
app = FastAPI()
client = MongoClient("mongodb+srv://mrbarboza:development@development-xi2j5.mongodb.net/test?retryWrites=true&w=majority")
db = client['spot-location']


# Models
class User(BaseModel):
    email: str


# Routes
@app.post('/sessions/')
def sessions_store(user: User):
    stored_user = db["User"].find_one({"email": user.email})
    if not stored_user:
        stored_user = db["User"].insert_one({"email": user.email})
    return Response(content=str(stored_user), media_type="application/json")