from flask import Flask, jsonify
from usuario import Usuario
from administrador import Administrador

app = Flask(__name__)

u = Usuario("Gabriel", "gabriel@exemplo.com")
a = Administrador("Admin", "admin@exemplo.com")
users = [a, u]


@app.route('/')
def index():
    return '<h1>Flask configurado</h1>'


@app.route('/api/users/')
def list_users():
    users_dict = []
    for user in users:
        users_dict.append(user.__dict__)
    return jsonify(users_dict)
