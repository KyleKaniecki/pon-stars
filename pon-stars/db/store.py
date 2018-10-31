from .base import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Store(BaseModel):

    __tablename__ = 'stores'

    id = Column(Integer, primary_key=True)
    store_type = Column(Integer)
    zip_code = Column(String)

    coupons = relationship("Coupon", back_populates="store", cascade="all, delete, delete-orphan")
