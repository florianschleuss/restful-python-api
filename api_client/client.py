import requests
from requests.auth import HTTPBasicAuth

r = requests


def main():
    response = r.get('http://localhost:5000/api/v1/test')
    print(response.text)

    response = r.post(
        'http://localhost:5000/api/v1/name/welcome', json={"name": "Flo"})
    print(response.text)

    response = r.get('http://localhost:5000/api/v1/auth',
                     auth=HTTPBasicAuth('demo', 'demo'))
    print(response.text)


if __name__ == "__main__":
    main()
