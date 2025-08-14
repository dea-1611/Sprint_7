import pytest
from Sprint_7.api import CourierAPI
from Sprint_7.helpers import create_random_login, create_random_password, create_random_firstname
@pytest.fixture
def random_courier():
    courier_data = {
        'login': create_random_login(),
        'password': create_random_password(),
        'firstName': create_random_firstname()
    }
    yield courier_data
    login_response = CourierAPI.login_courier({
        'login': courier_data['login'],
        'password': courier_data['password']
    })
    if login_response.status_code == 200:
        courier_id = login_response.json()['id']
        CourierAPI.delete_courier(courier_id)
