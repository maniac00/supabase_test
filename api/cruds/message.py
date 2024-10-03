from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

import api.models.message as message_model
import api.schemas.message as message_schema


async def create_message(
    db: AsyncSession, message_create: message_schema.MessageCreate
) -> message_model.Message:
    message = message_model.Message(**message_create.dict())
    db.add(message)
    await db.commit()
    await db.refresh(message)
    return message


async def get_message(db: AsyncSession, message_key: int) -> message_model.Message | None:
    result: Result = await db.execute(
        select(message_model.Message).filter(message_model.Message.message_key == message_key)
    )
    return result.scalars().first()
