from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from base_class import Base


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True)
    name = Column(String, 50)
    email = Column(String, 50)
    phone = Column(String, 50)
    address = Column(String, 100)
    country = Column(String, 50)
    imcs = relationship("IMC", back_populates="user")

