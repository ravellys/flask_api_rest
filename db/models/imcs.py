from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from base_class import Base


class IMC(Base):
    __tablename__ = "users"
    imc_id = Column(Integer, primary_key=True)
    altura = Column(Float, 50)
    peso = Column(String, 50)
    imc = Column(String, 50)
    data = Column(String, 100)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    user = relationship("User", back_populates="imcs")
