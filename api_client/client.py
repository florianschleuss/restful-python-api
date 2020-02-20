import requests
from requests.auth import HTTPBasicAuth

r = requests

class api_client:

    def __init__(self, base_url):
        self.API_BASE_URL = base_url

    def post(self, resource, data):
        response = r.post(
        self.API_BASE_URL + resource, json=data)
        return response

    def patch(self, resource, data):
        response = r.patch(
        self.API_BASE_URL + resource, json=data)
        return response

    def get(self, resource):
        response = r.get(self.API_BASE_URL + resource)
        return response

    def delete(self, resource):
        response = r.delete(self.API_BASE_URL + resource)
        return response




def main():
    response = r.post(
        'http://localhost:5000/api/v1/customer/hpe', json={"name": "Hewlette Packard Enterprise"})
    print(response.text)

    response = r.get('http://localhost:5000/api/v1/customer/hpe')
    print(response.text)

    response = r.patch(
        'http://localhost:5000/api/v1/customer/hpe', json={"name": "Hewlett Packard Enterprise"})
    print(response.text)

    response = r.get('http://localhost:5000/api/v1/customer/hpe')
    print(response.text)

    response = r.delete('http://localhost:5000/api/v1/customer/hpe')
    print(response.text)

    response = r.get('http://localhost:5000/api/v1/customers')
    print(response.text)

    response = r.get('http://localhost:5000/api/v1/auth',
                     auth=HTTPBasicAuth('demo', 'demo'))
    print(response.text)


if __name__ == "__main__":
    main()
