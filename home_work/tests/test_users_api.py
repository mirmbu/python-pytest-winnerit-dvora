import requests
import pytest
from assertpy import assert_that


def test_get_all_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users", verify=False)
    assert response.status_code == 200
    print(list(response))
    assert len(list(response)) == 10

def test_get_user_by_id():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1", verify=False)
    assert response.status_code == 200
    response_body = response.json()
    assert_that(response_body["name"]).is_equal_to("Leanne Graham")
    assert_that(response_body["email"]).is_equal_to("Sincere@april.biz")

def test_user_not_found():
    response = requests.get("https://jsonplaceholder.typicode.com/users/999", verify=False)
    assert response.status_code == 404

def test_structure_user():
    response = requests.get("https://jsonplaceholder.typicode.com/users/3", verify=False)
    response_body = response.json()
    assert_that(response_body).contains_key("id")
    assert_that(response_body).contains_key("username")
    assert_that(response_body["address"]).contains_key("street")
    assert_that(response_body["address"]["geo"]).contains_key("lat")
    assert_that(response_body["company"]).contains_key("catchPhrase")

data_json = [
    (3, "Clementine Bauch"),
    (5, "Chelsey Dietrich"),
    (9, "Glenna Reichert"),
    (7, "Kurtis Weissnat"),
    (10, "Clementina DuBuque")
]

@pytest.mark.parametrize("id, name", data_json)
def test_multiple_users(id, name):
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{id}", verify=False)
    response_body = response.json()
    assert_that(response_body["name"]).is_equal_to(name)

