from sanic.response import json, HTTPResponse
import status_code

try:
    from ujson import dumps as json_dumps
except ImportError:
    from json import dumps


class LouisJsonResponse:

    # def __init__(self, data=None, code=status_code.OK, msg='success', count=0):
    #
    #     if data:
    #         if count > 0:
    #             self.data = {"code": code, "msg": msg, "data": data, "count": count}
    #         else:
    #             self.data = {"code": code, "msg": msg, "data": data}
    #     else:
    #         self.data = {"code": code, "msg": msg}
    #     super().__init__()
    #
    #     print('****', self.data)

    @classmethod
    def json(cls,
             body,
             status=200,
             headers=None,
             count=0,
             code=status_code.OK,
             msg='success',
             content_type="application/json",
             dumps=json_dumps,
             **kwargs):

        if body:

            if count > 0:
                data = {"code": code, "msg": msg, "data": body, "count": count}
            else:
                data = {"code": code, "msg": msg, "data": body}
        else:
            data = {"code": code, "msg": msg}


        return HTTPResponse(
            dumps(data,**kwargs),
            headers=headers,
            status=status,
            content_type=content_type
        )

    # def __call__(self, *args, **kwargs):
    #     print('****',self.data)
    #     return json(self.data)
