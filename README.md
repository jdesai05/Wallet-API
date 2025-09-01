# 💳 Wallet API

[![Demo Video](https://img.shields.io/badge/▶️%20Watch-Demo%20Video-blue)](https://drive.google.com/file/d/1luGImfWMKTnNoNXHpcc7MBlQz2dKO7z7/view)

A simple Wallet Management System built with **FastAPI**.  
This project provides APIs to manage users, update their wallet balances, and fetch transaction history.  

---

## 🚀 Features
- **Create User** → Add new users with name, email, phone.  
- **List Users** → View all users with wallet balances.  
- **Update Wallet** → Credit/debit a user’s wallet and log the transaction.  
- **Fetch Transactions** → Get all wallet transactions for a specific user.  
- **Swagger UI** → Interactive API documentation at `/docs`.  

---

## 🛠 Tech Stack
- **FastAPI** – Web framework  
- **SQLite** – Database (via SQLAlchemy ORM)  
- **Pydantic** – Data validation & serialization  
- **Uvicorn** – ASGI server  

---

## 📦 Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/jdesai05/Wallet-API.git
