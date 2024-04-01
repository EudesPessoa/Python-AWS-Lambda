import json

from app import app
from chalice.test import Client


def test_create_person():
    with Client(app) as client:
        response = client.http.post(
                    '/consumers/person',
                    body= json.dumps({"name": "usuário5", "phone": "47999999995"}),
                    headers={"Content-Type": "application/json"}
                    )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200


def test_update_person():
    with Client(app) as client:
        response = client.http.put(
                        '/consumers/person',
                        body=json.dumps({"name": "usuário1", "phone": "47999999999"}),
                        headers={"Content-Type": "application/json"}
                    )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200


def test_delete_person():
    with Client(app) as client:
        response = client.http.delete(
                        '/consumers/person',
                        body=json.dumps({"name": "usuário1", "phone": "47999999999"}),
                        headers={"Content-Type": "application/json"}
                    )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200


def test_get_persons():
    with Client(app) as client:
        response = client.http.get(
                        '/consumers/persons'
                    )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200


def test_get_person():
    with Client(app) as client:
        response = client.http.get(
                        '/consumers/person/1'
                    )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200


def test_create_company():
    with Client(app) as client:
        response = client.http.post(
                        '/consumers/company',
                        body=json.dumps({"name": "empresa1", "telefone": "47999999999"}),
                        headers={"Content-Type": "application/json"}
                    )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200


def test_update_company():
    with Client(app) as client:
        response = client.http.put(
                        '/consumers/company',
                        body=json.dumps({"name": "empresa1", "telefone": "47999999999"}),
                        headers={"Content-Type": "application/json"}
                    )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200


def test_delete_company():
    with Client(app) as client:
        response = client.http.delete(
                        '/consumers/company',
                        body=json.dumps({"name": "empresa1", "telefone": "47999999999"}),
                        headers={"Content-Type": "application/json"}
                    )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200


def test_get_companies():
    with Client(app) as client:
        response = client.http.get(
                        '/consumers/companies'
                    )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200


def test_get_company():
    with Client(app) as client:
        response = client.http.get(
                        '/consumers/company/1'
                    )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200