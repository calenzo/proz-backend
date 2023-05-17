from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from lib.routes import notification_routes

from database.settings import create_tables


create_tables()


app = FastAPI(app_name="proz")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(notification_routes.router)
