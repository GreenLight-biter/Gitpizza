from fastapi import FastAPI
from routes import router
from database import create_tables

create_tables()


app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Pizza API работает, это главная страница"}


app.include_router(router)    