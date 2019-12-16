from sanic import Sanic
from model import base_model

app = Sanic(__name__)
# todo 了解一下里面的参数用途

db = base_model.db

@app.middleware('request')
async def handle_request(request):
    db.connect()

@app.middleware('response')
async def handle_response(request, response):
    if not db.is_closed():
        db.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
