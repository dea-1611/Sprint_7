import allure
import pytest
from Sprint_7.data import Data, ErrorMessages
from Sprint_7.api import CourierAPI

class TestCourierLogin:
    @allure.title('Успешная аутентификация курьера')
    def test_courier_login_success(self):
        response = CourierAPI.login_courier({
            'login': Data.valid_login,
            'password': Data.valid_password
        })
        assert response.status_code == 200
        assert 'id' in response.json()

    @allure.title('Аутентификация с неверным логином')
    def test_courier_login_invalid_login(self):
        response = CourierAPI.login_courier({
            'login': 'invalid_login',
            'password': Data.valid_password
        })
        assert response.status_code == 404
        assert response.json()['message'] == ErrorMessages.ACCOUNT_NOT_FOUND

    @allure.title('Аутентификация с неверным паролем')
    def test_courier_login_invalid_password(self):
        response = CourierAPI.login_courier({
            'login': Data.valid_login,
            'password': 'invalid_password'
        })
        assert response.status_code == 404
        assert response.json()['message'] == ErrorMessages.ACCOUNT_NOT_FOUND

    @allure.title('Аутентификация без логина')
    def test_courier_login_missing_login(self):
        response = CourierAPI.login_courier({'password': Data.valid_password})
        assert response.status_code == 400
        assert response.json()['message'] == ErrorMessages.NOT_ENOUGH_DATA_FOR_LOGIN

    @allure.title('Аутентификация без пароля')
    def test_courier_login_missing_password(self):
        response = CourierAPI.login_courier({'login': Data.valid_login})
        assert response.status_code in [400, 504]
        if response.status_code == 400:
            assert response.json()['message'] == ErrorMessages.NOT_ENOUGH_DATA_FOR_LOGIN

