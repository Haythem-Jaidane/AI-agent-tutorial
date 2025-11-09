from sqlalchemy import Column, Integer, String, Float, DateTime
from config.database import Base
from datetime import datetime

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    amount = Column(Float)
    date = Column(DateTime, default=datetime.now)
    type = Column(String, index=True)  # 'expense' or 'income'
    category = Column(String, nullable=True)
