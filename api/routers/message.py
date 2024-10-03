from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

import api.schemas.message as message_schema
import api.cruds.message as message_crud
from api.db import get_db

router = APIRouter()

@router.get("/messages", response_model=list[message_schema.Message])
async def read_messages():
    return [message_schema.Message(message_key=1, content="안녕하세요.")]

@router.post("/messages", response_model=message_schema.MessageCreateResponse)
async def create_message(
    message_body: message_schema.MessageCreate, db: AsyncSession = Depends(get_db)
    ):
    return await message_crud.create_message(db, message_body)
