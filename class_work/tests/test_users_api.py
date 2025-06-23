import requests
import pytest
from assertpy import assert_that
from dotenv import load_dotenv
import os

load_dotenv()

headers = {"x-api-key": os.getenv("X_API_KEY")}
base_api_url = "https://reqres.in/api"

def test_get_not_found_user():
    response = requests.get(f"{base_api_url}/users/90", verify=False, headers=headers)
    assert response.status_code == 404
    assert response.reason == "Not Found"


def test_login_successful():
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = requests.post(f"{base_api_url}/login", verify=False, json=payload, headers=headers)
    assert response.status_code == 200
    assert response.reason == "OK"
    response_body = response.json()
    assert_that(response_body).contains_key("token")

def test_register_unsuccessful():
    payload = {
        "email": "bbb@gmail.com"
    }
    response = requests.post(f"{base_api_url}/register", verify=False, json=payload, headers=headers)
    assert response.status_code == 400
    response_body = response.json()
    assert_that(response_body).contains_key("error")
    assert_that(response_body["error"]).is_equal_to("Missing password")

