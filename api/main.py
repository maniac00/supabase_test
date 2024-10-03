from fastapi import FastAPI
from supabase import create_client, Client

from api.routers import message

app = FastAPI()
url = ""
key = ""

app.include_router(message.router)

supabase: Client = create_client(url, key)