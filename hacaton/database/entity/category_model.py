from database.base import Base
from sqlalchemy import Column, Integer, String


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    title = Column(String(4096), nullable=False, unique=False)

    def __init__(self, title):
        self.title = title
