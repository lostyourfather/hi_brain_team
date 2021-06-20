"""add_data

Revision ID: 22c2c9cd263d
Revises: 654da5778cac
Create Date: 2021-06-20 00:27:07.281290

"""
import os

from alembic import op
import sqlalchemy as sa
import pandas as pd
from database.entity.courses_model import Course
from database.entity.review_model import Review
from database.entity.category_model import Category
from database.base import Session

revision = '22c2c9cd263d'
down_revision = '654da5778cac'
branch_labels = None
depends_on = None


def upgrade():
    session = Session()
    df_review = pd.read_csv("versions/data/prediction.csv")
    df_course = pd.read_csv("versions/data/fin_course.csv")
    df_vuz = pd.read_csv("versions/data/fin_vuz.csv")
    categories = set()
    for i, row in df_course.iterrows():
        if row["category"] not in categories:
            category = Category(title=row["category"])
            session.add(category)
            categories.add(row["category"])
        else:
            continue
    session.commit()
    for index, row in df_course.iterrows():
        category = session.query(Category).filter(Category.title == row["category"]).first()
        course = Course(course_id=row["id"], title=row["title_of_program"], category=category.id, provider=row["provider"])
        session.add(course)
    session.commit()
    for index, row in df_vuz.iterrows():
        category = session.query(Category).filter(Category.title == row["category"]).first()
        course = Course(course_id=row["id"], title=row["title_of_program"], category=category.id, provider=row["provider"])
        session.add(course)
    session.commit()
    for index, row in df_review.iterrows():
        course = session.query(Course).filter(Course.course_id == row["COURSE_ID"]).first()
        if course is not None:
            review = Review(text=row["Merged_data"], course=course.id, rating=row["predicted_values"])
            session.add(review)
    session.commit()


def downgrade():
    pass
