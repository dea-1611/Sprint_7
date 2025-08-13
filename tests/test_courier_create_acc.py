import requests
import allure
import pytest
from ..data import Data
from ..urls import Urls
from helpers import create_random_login, create_random_password, create_random_firstname


class TestCourierCreate:

    @allure.title('Успешное создание аккаунта курьера с валидными данными')
    def test_create_courier_account_success(self):
        payload = {
            'login': create_random_login(),
            'password': create_random_password(),
            'firstName': create_random_firstname()
        }
        response = requests.post(Urls.URL_courier_create, data=payload)
        assert response.status_code == 201 and response.json() == {'ok': True}

    @allure.title('Получение ошибки при повторном использовании логина для создания курьера')
    def test_create_courier_account_login_taken_conflict(self):
        payload = {
            'login': Data.valid_login,
            'password': create_random_password(),
            'firstName': create_random_firstname()
        }
        response = requests.post(Urls.URL_courier_create, data=payload)
        expected_response = {
            'code': 409,
            'message': 'Этот логин уже используется. Попробуйте другой.'
        }
        assert response.status_code == 409 and response.json() == expected_response

    @pytest.mark.parametrize('empty_credentials', [
        {'login': '', 'password': create_random_password(), 'firstName': create_random_firstname()},
        {'login': create_random_login(), 'password': '', 'firstName': create_random_firstname()}
    ])
    def test_create_courier_account_with_empty_required_fields(self, empty_credentials):
        response = requests.post(Urls.URL_courier_create, data=empty_credentials)
        expected_response = {
            'code': 400,
            'message': 'Недостаточно данных для создания учетной записи'
        }
        assert response.status_code == 400 and response.json() == expected_response