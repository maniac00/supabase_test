from sqlalchemy import Column, Integer, String

from api.db import Base

class Message(Base):
    __tablename__ = 'messages'
 
    message_key = Column(Integer, primary_key=True)
    content = Column(String(1024))