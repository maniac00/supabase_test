from pydantic import BaseModel, Field

class MessageBase(BaseModel):
    content: str

class MessageCreate(MessageBase):
    pass

class MessageCreateResponse(MessageBase):
    message_key: int

    class Config:
        orm_mode = True


class Message(MessageBase):
    message_key: int

    class Config:
        orm_mode = True
