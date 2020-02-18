import json

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_restful import Api, reqparse

import calculatorController
import nameController

users = {
    'demo': 'demo',
}
app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()

name = nameController.Controller()
calc = calculatorController.Controller()


@auth.verify_password
def verify_password(username, password):
    if username in users:
        return users[username] == password
    return False


@app.route('/api/v1/test', methods=['GET'])
def connection_test():
    return jsonify({'message': 'works'})


@app.route('/api/v1/name/welcome', methods=['POST'])
def welcome():
    data = request.json
    return jsonify({'message': name.welcome(data['name'])})


@app.route('/api/v1/auth', methods=['GET'])
@auth.login_required
def authentification_test():
    return jsonify({'message': 'authenticated'})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
