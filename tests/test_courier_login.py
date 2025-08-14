import allure
import pytest
from Sprint_7.data import Data, ErrorMessages
from Sprint_7.api import CourierAPI

class TestCourierLogin:
    @allure.title('Успешная аутентификация курьера')
    @allure.step('Авторизация с валидными данными. Проверка кода и тела ответа.')
    def test_courier_login_success(self):
        response = CourierAPI.login_courier({
            'login': Data.valid_login,
            'password': Data.valid_password
        })
        assert response.status_code == 200
        assert 'id' in response.json()

    @allure.title('Аутентификация с неверным логином')
    @allure.step('Попытка входа с невалидным логином. Проверка кода и тела ответа.')
    def test_courier_login_invalid_login(self):
        response = CourierAPI.login_courier({
            'login': 'invalid_login',
            'password': Data.valid_password
        })
        assert response.status_code == 404
        assert response.json()['message'] == ErrorMessages.ACCOUNT_NOT_FOUND

    @allure.title('Аутентификация с неверным паролем')
    @allure.step('Попытка входа с невалидным паролем. Проверка кода и тела ответа.')
    def test_courier_login_invalid_password(self):
        response = CourierAPI.login_courier({
            'login': Data.valid_login,
            'password': 'invalid_password'
        })
        assert response.status_code == 404
        assert response.json()['message'] == ErrorMessages.ACCOUNT_NOT_FOUND

    @allure.title('Аутентификация с пустым логином')
    @allure.step('Попытка входа с пустым логином. Проверка кода и тела ответа.')
    def test_courier_login_empty_login(self):
        response = CourierAPI.login_courier({
            'login': '',
            'password': Data.valid_password
        })
        assert response.status_code == 400
        assert response.json()['message'] == ErrorMessages.NOT_ENOUGH_DATA_FOR_LOGIN

    @allure.title('Аутентификация с пустым паролем')
    @allure.step('Попытка входа с пустым паролем. Проверка кода и тела ответа.')
    def test_courier_login_empty_password(self):
        response = CourierAPI.login_courier({
            'login': Data.valid_login,
            'password': ''
        })
        assert response.status_code == 400
        assert response.json()['message'] == ErrorMessages.NOT_ENOUGH_DATA_FOR_LOGIN


