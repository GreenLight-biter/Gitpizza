from fastapi import FastAPI
from routes import router
from database import create_tables

create_tables()


app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Добро пожаловать в Pizza API!"}


app.include_router(router)    