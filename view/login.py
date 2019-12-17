from sanic.response import text, HTTPResponse
from sanic.views import HTTPMethodView
from sanic import Blueprint
from model.blog.dairy import Dairy
from playhouse.shortcuts import model_to_dict
from utils.response import LouisJsonResponse

bp = Blueprint('index')


class SimpleView(HTTPMethodView):
    async def post(self, request):
        obj = Dairy.select().where(Dairy.content == '123').get()
        res = model_to_dict(obj)
        # res = [1,2,3]
        # print(res)
        return LouisJsonResponse.json(res)


bp.add_route(SimpleView.as_view(), '/')

