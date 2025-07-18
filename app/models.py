from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


Base = declarative_base()


class OperationRequest(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True)
    operation = Column(String)
    input = Column(String)
    result = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)


class OperationInput(BaseModel):
    operation: str
    number: int
