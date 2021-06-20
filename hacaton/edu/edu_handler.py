import traceback
import falcon
import json
from database.entity.review_model import Review
from database.entity.category_model import Category
from database.entity.courses_model import Course
from database.base import Session


class EduHandler(object):

    def on_get(self, req, resp):
        session = Session()
        param = req.get_param('category')
        category = session.query(Category).filter(Category.title==param).first()
        courses = session.query(Course).filter(Course.category==category.id).all()
        courses_dict = [course.__dict__ for course in courses]
        response = ""
        cnt = 0
        for obj in courses_dict:
            if obj["title"] != "NaN" and len(obj["title"]) < 100:
                cnt += 1
                response += f"{cnt}. Название: {obj['title']}\nОрганизатор: {obj['provider']}\n\n"
        resp.body = response
        resp.status = falcon.HTTP_200
