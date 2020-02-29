import json

from flask import Flask, jsonify, request #jsonify erstellt HTTP response 
from flask_httpauth import HTTPBasicAuth
from flask_restful import Api, reqparse

import locationController
import customerController

users = {
    'demo': 'demo',
}
app = Flask(__name__) #Erzeugt ein App Objekt aus Flask
api = Api(app)
auth = HTTPBasicAuth()

customer_controller = customerController.Controller()
location_controller = locationController.Controller()


@auth.verify_password
def verify_password(username, password):
    if username in users:
        return users[username] == password
    return False


@app.route('/api/v1/test', methods=['GET'])
def connection_test():
    return jsonify({'message': 'works'})


@app.route('/api/v1/customers', methods=['GET'])
@auth.login_required
def customers():
    return jsonify(customer_controller.get_customers())


@app.route('/api/v1/locations', methods=['GET'])
@auth.login_required
def locations():
    return jsonify(location_controller.get_locations(customer_controller.get_customers()))


@app.route('/api/v1/customer/<customer_id>', methods=['GET','POST', 'PATCH', 'DELETE']) #Service führt @POST, @GET, @PATCH @DELETE aus und gibt Ergebnis zurück
def customer(customer_id):
    if request.method == 'GET':
        return jsonify(customer_controller.get_customer(customer_id))
    elif request.method == 'POST':
        data = request.json
        return jsonify(customer_controller.post_customer(customer_id, data))
    elif request.method == 'PATCH':
        data = request.json
        return jsonify(customer_controller.patch_customer(customer_id, data))
    elif request.method == 'DELETE':
        return jsonify(customer_controller.delete_customer(customer_id))
    else:
        return jsonify({'message': 'error occurred'}), 500
    


@app.route('/api/v1/auth', methods=['GET'])
@auth.login_required
def authentification_test():
    return jsonify({'message': 'authenticated'})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True) #starts the web server and ready to handle the request
