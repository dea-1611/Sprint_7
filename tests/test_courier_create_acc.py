import allure
import pytest
from Sprint_7.data import Data, ErrorMessages
from Sprint_7.api import CourierAPI
from Sprint_7.helpers import create_random_login, create_random_password, create_random_firstname

class TestCourierCreation:
    @pytest.fixture
    def random_courier(self):
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

    @allure.title('Успешное создание курьера')
    def test_create_courier_success(self, random_courier):
        response = CourierAPI.create_courier(random_courier)
        assert response.status_code == 201
        assert response.json() == {'ok': True}

    @allure.title('Создание дубликата курьера')
    def test_create_duplicate_courier(self):
        response = CourierAPI.create_courier(Data.valid_courier_data)
        assert response.status_code == 409
        assert response.json()['message'] == ErrorMessages.LOGIN_EXISTS

    @allure.title('Создание курьера без обязательных полей')
    def test_create_courier_missing_fields(self):
        response = CourierAPI.create_courier({'login': 'test_login'})
        assert response.status_code in [400, 409]
        if response.status_code == 400:
            assert response.json()['message'] == ErrorMessages.NOT_ENOUGH_DATA_FOR_CREATE
        else:
            assert response.json()['message'] == ErrorMessages.LOGIN_EXISTS


