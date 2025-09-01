from pydantic import BaseModel
from typing import List
from datetime import datetime

# Transaction Schema
class TransactionBase(BaseModel):
    amount: float

class TransactionCreate(TransactionBase):
    pass

class TransactionResponse(TransactionBase):
    id: int
    user_id: int
    timestamp: datetime

    class Config:
        orm_mode = True


# User Schema
class UserBase(BaseModel):
    name: str
    email: str
    phone: str

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int
    wallet_balance: float
    transactions: List[TransactionResponse] = []

    class Config:
        orm_mode = True
