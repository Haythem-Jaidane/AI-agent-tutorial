from sqlalchemy.orm import Session
from models import models
from requests import transactions as schemas
from datetime import datetime

# Transaction CRUD
def create_transaction(db: Session, transaction: schemas.TransactionCreate):
    db_transaction = models.Transaction(
        description=transaction.description,
        amount=transaction.amount,
        date=transaction.date if transaction.date else datetime.now(),
        type=transaction.type,
        category=transaction.category
    )
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

def get_transactions(db: Session, type: str = None, skip: int = 0, limit: int = 100):
    query = db.query(models.Transaction)
    if type:
        query = query.filter(models.Transaction.type == type)
    return query.offset(skip).limit(limit).all()

def get_transaction(db: Session, transaction_id: int):
    return db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()

def update_transaction(db: Session, transaction_id: int, transaction: schemas.TransactionCreate):
    db_transaction = db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()
    if db_transaction:
        db_transaction.description = transaction.description
        db_transaction.amount = transaction.amount
        db_transaction.date = transaction.date if transaction.date else db_transaction.date
        db_transaction.type = transaction.type
        db_transaction.category = transaction.category
        db.commit()
        db.refresh(db_transaction)
    return db_transaction

def delete_transaction(db: Session, transaction_id: int):
    db_transaction = db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()
    if db_transaction:
        db.delete(db_transaction)
        db.commit()
        return True
    return False
