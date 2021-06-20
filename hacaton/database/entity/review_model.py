from database.base import Base
from sqlalchemy import Column, Integer, String, Text, ForeignKey


class Review(Base):
    __tablename__ = 'review'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    text = Column(Text, nullable=False, unique=False)
    course = Column(Integer, ForeignKey("course.id", ondelete="CASCADE"), nullable=False, unique=False)
    rating = Column(Integer, nullable=False, unique=False)

    def __init__(self, text, course, rating):
        self.text = text
        self.course = course
        self.rating = rating
