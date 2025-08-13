import requests
import allure
import pytest
from ..data import Data
from ..urls import URL_COURIER_CREATE, URL_COURIER_LOGIN, URL_COURIER_DELETE
from ..helpers import create_random_login, create_random_password, create_random_firstname


class TestCourierCreation:
    @allure.title('Успешное создание курьера')
    def test_create_courier_success(self):
        courier_data = {
            'login': create_random_login(),
            'password': create_random_password(),
            'firstName': create_random_firstname()
        }

        response = requests.post(URL_COURIER_CREATE, data=courier_data)
        assert response.status_code == 201
        assert response.json() == {'ok': True}

        login_response = requests.post(URL_COURIER_LOGIN, data={
            'login': courier_data['login'],
            'password': courier_data['password']
        })
        courier_id = login_response.json()['id']
        requests.delete(f"{URL_COURIER_DELETE}/{courier_id}")

    @allure.title('Создание дубликата курьера')
    def test_create_duplicate_courier(self):
        response = requests.post(URL_COURIER_CREATE, data=Data.valid_courier_data)
        assert response.status_code == 409
        assert response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'

    @allure.title('Создание курьера без обязательных полей')
    def test_create_courier_missing_fields(self):
        response = requests.post(URL_COURIER_CREATE, data=Data.courier_data_without_name)
        assert response.status_code == 409
        assert response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'

