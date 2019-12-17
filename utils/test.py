from utils.uid import gen_id
res = gen_id()
# print(res)


from sanic import Sanic
from sanic_restplus import Api, Resource, fields
from sanic_restplus.restplus import restplus
from spf import SanicPluginsFramework
app = Sanic(__name__)
spf = SanicPluginsFramework(app)
rest_assoc = spf.register_plugin(restplus)

api = Api(version='1.0', title='TodoMVC API',
          description='A simple TodoMVC API')

ns = api.namespace('todos', description='TODO operations')

todo = api.model('Todo', {
    'id': fields.Integer(readOnly=True, description='The task unique identifier'),
    'task': fields.String(required=True, description='The task details')
})


class TodoDAO(object):
    def __init__(self):
        self.counter = 0
        self.todos = []

    def get(self, id):
        for todo in self.todos:
            if todo['id'] == id:
                return todo
        api.abort(404, "Todo {} doesn't exist".format(id))

    def create(self, data):
        todo = data
        todo['id'] = self.counter = self.counter + 1
        self.todos.append(todo)
        return todo

    def update(self, id, data):
        todo = self.get(id)
        todo.update(data)
        return todo

    def delete(self, id):
        todo = self.get(id)
        self.todos.remove(todo)


DAO = TodoDAO()
DAO.create({'task': 'Build an API'})
DAO.create({'task': '?????'})
DAO.create({'task': 'profit!'})


@ns.route('/')
class TodoList(Resource):
    '''Shows a list of all todos, and lets you POST to add new tasks'''

    @ns.doc('list_todos')
    @ns.marshal_list_with(todo)
    async def get(self, request):
        '''List all tasks'''
        return DAO.todos

    @ns.doc('create_todo')
    @ns.expect(todo)
    @ns.marshal_with(todo, code=201)
    async def post(self, request):
        '''Create a new task'''
        return DAO.create(request.json), 201


@ns.route('/<id:int>')
@ns.response(404, 'Todo not found')
@ns.param('id', 'The task identifier')
class Todo(Resource):
    '''Show a single todo item and lets you delete them'''

    @ns.doc('get_todo')
    @ns.marshal_with(todo)
    async def get(self, request, id):
        '''Fetch a given resource'''
        return DAO.get(id)

    @ns.doc('delete_todo')
    @ns.response(204, 'Todo deleted')
    async def delete(self, request, id):
        '''Delete a task given its identifier'''
        DAO.delete(id)
        return '', 204

    @ns.expect(todo)
    @ns.marshal_with(todo)
    async def put(self, request, id):
        '''Update a task given its identifier'''
        return DAO.update(id, request.json)

rest_assoc.api(api)

if __name__ == '__main__':
    # app.run(debug=True, auto_reload=False)
    class X(object):
        def __init__(self, a, b, range):
            self.a = a
            self.b = b
            self.range = range

        def __call__(self, a, b):
            self.a = a
            self.b = b
            print('__call__ with （{}, {}）'.format(self.a, self.b))

        def __del__(self, a, b, range):
            del self.a
            del self.b
            del self.range

    x = X(1,2,3)
    x(3,4)
