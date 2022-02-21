from flask import Flask, jsonify, abort, request, json
from usuario import Usuario
from administrador import Administrador

app = Flask(__name__)

u = Usuario("Gabriel", "gabriel@exemplo.com")
a = Administrador("Admin", "admin@exemplo.com")
users = [a, u]


@app.errorhandler(404)
def handle_not_found(error):
    return (jsonify(error=str(error)), 404)


@app.errorhandler(400)
def handle_bad_request(error):
    return (jsonify(error=str(error)), 400)


@app.route('/')
def index():
    return '<h1>Flask configurado</h1>'


@app.route('/api/users/')
def list_users():
    users_dict = []
    for user in users:
        users_dict.append(user.__dict__)
    return jsonify(users_dict)


@app.route('/api/users/', methods=['POST'])
def create_user():
    data = json.loads(request.data)
    email = data.get('email')
    nome = data.get('nome')
    isAdmin = data.get('isAdmin')

    if not email:
        abort(400, "'email': O email é obrigatório")

    if not nome:
        abort(400, "'nome': O nome é obrigatório")

    if isAdmin == True:
        user = Administrador(nome=nome, email=email)
    else:
        user = Usuario(nome=nome, email=email)

    users.append(user)

    return {
        "id": user.id,
        "url": f'/api/users/{user.id}'
    }


def get_user_or_404(id):
    for user in users:
        if user.id == id:
            return user
    abort(404, 'Usuário não encontrado')


@app.route('/api/users/<int:id>/')
def get_user(id):
    user = get_user_or_404(id)
    return jsonify(user.__dict__)


@app.route('/api/users/<int:id>/', methods=['DELETE'])
def delete_user(id):
    user = get_user_or_404(id)
    users.remove(user)
    return jsonify(id=id)


@app.route('/api/users/<int:id>/', methods=['PUT'])
def edit_user(id):
    data = request.get_json()
    email = data.get('email')
    nome = data.get('nome')

    if not email:
        abort(400, "'email': O email é obrigatório")

    if not nome:
        abort(400, "'nome': O nome é obrigatório")

    user = get_user_or_404(id)
    user.email = email
    user.nome = nome

    return user.__dict__


@app.route('/api/users/<int:id>/', methods=['PATCH'])
def edit_user_partial(id):
    data = request.get_json()
    email = data.get('email')
    nome = data.get('nome')

    user = get_user_or_404(id)
    if 'email' in data.keys():
        if not email:
            abort(400, "'email': O email é obrigatório")
        user.email = email

    if 'nome' in data.keys():
        if not nome:
            abort(400, "'nome': O nome é obrigatório")
        user.nome = nome

    return user.__dict__
