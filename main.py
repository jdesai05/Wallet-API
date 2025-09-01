from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from database import SessionLocal, Base, engine
import models, schemas

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Wallet API",
    description="Simple Wallet Management System",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Welcome to the Wallet API"}

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ------------------- ROUTES -------------------

# 1. List Users
@app.get("/users", response_model=list[schemas.UserResponse])
def list_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users


# 2. Create User
@app.post("/users", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(name=user.name, email=user.email, phone=user.phone)
    db.add(db_user)
    try:
        db.commit()
        db.refresh(db_user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Email or phone already exists")
    return db_user


# 3. Get User Transactions
@app.get("/users/{user_id}/transactions", response_model=list[schemas.TransactionResponse])
def get_transactions(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user.transactions


# 4. Update Wallet
@app.post("/users/{user_id}/wallet", response_model=schemas.UserResponse)
def update_wallet(user_id: int, transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Update wallet balance
    user.wallet_balance += transaction.amount

    # Record transaction
    new_transaction = models.Transaction(user_id=user.id, amount=transaction.amount)
    db.add(new_transaction)
    db.commit()
    db.refresh(user)

    return user
