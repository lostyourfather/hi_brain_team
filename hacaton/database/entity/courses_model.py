from database.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    course_id = Column(Integer, nullable=False, unique=False)
    title = Column(String(4096), nullable=False, unique=False)
    category = Column(Integer, ForeignKey("category.id", ondelete="CASCADE"))
    provider = Column(String(4096), nullable=False, unique=False)

    def __init__(self, course_id, title, category, provider):
        self.course_id = course_id
        self.title = title
        self.category = category
        self.provider = provider
