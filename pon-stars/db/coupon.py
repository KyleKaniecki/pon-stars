from .base import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

class Coupon(BaseModel):

    __tablename__ = 'coupons'

    id = Column(Integer, primary_key=True)
    brand = Column(String)
    discount = Column(Float)
    store_id = Column(Integer, ForeignKey('stores.id'))
    
    store = relationship("Store", back_populates="coupons")


