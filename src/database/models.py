from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
import datetime

class Opportunity(Base):
    __tablename__ = "opportunities"

    id = Column(Integer, primary_key=True, index=True)
    event = Column(String, index=True)
    platform1 = Column(String)
    platform2 = Column(String)
    profit = Column(Float)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    bets = relationship("Bet", back_populates="opportunity")

class Bet(Base):
    __tablename__ = "bets"

    id = Column(Integer, primary_key=True, index=True)
    opportunity_id = Column(Integer, ForeignKey("opportunities.id"))
    platform = Column(String)
    event = Column(String)
    outcome = Column(String)
    stake = Column(Float)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    opportunity = relationship("Opportunity", back_populates="bets")