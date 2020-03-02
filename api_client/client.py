import requests
from requests.auth import HTTPBasicAuth

r = requests

class api_client:

    #Instanzierung
    def __init__(self, base_url):
        self.API_BASE_URL = base_url
        self.authentificiation = False

    #Authentifizierung
    def auth(self, name, passwd):
        self.name = name
        self.passwd = passwd
        self.authentificiation = True

    def post(self, resource, data):
        if self.authentificiation:
            response = r.post(
            self.API_BASE_URL + resource, json=data, auth=HTTPBasicAuth(self.name, self.passwd))
        else: 
            response = r.post(
            self.API_BASE_URL + resource, json=data)
        return response

    def patch(self, resource, data):
        if self.authentificiation:
            response = r.patch(
            self.API_BASE_URL + resource, json=data, auth=HTTPBasicAuth(self.name, self.passwd))
        else:
            response = r.patch(
            self.API_BASE_URL + resource, json=data)
        return response

    def get(self, resource):
        if self.authentificiation:
            response = r.get(
            self.API_BASE_URL + resource, auth=HTTPBasicAuth(self.name, self.passwd))
        else:
            response = r.get(self.API_BASE_URL + resource)
        return response

    def delete(self, resource):
        if self.authentificiation:
            response = r.delete(
            self.API_BASE_URL + resource, auth=HTTPBasicAuth(self.name, self.passwd))
        else:
            response = r.delete(self.API_BASE_URL + resource)
        return response
