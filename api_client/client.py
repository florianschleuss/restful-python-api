import requests
from requests.auth import HTTPBasicAuth

r = requests


def main():
    response = r.get('http://localhost:5000/api/v1/test')
    print(response.text)

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
