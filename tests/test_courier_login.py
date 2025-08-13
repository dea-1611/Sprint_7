import requests
import allure
import pytest
from ..data import Data
from ..urls import Urls
from helpers import create_random_login, create_random_password, create_random_firstname


class TestCourierLogin:

    @allure.title('Успешная аутентификация курьера при вводе валидных данных')
    def test_courier_login_success(self):
        response = requests.post(Urls.URL_courier_login, data=Data.valid_courier_data)
        assert response.status_code == 200 and 'id' in response.text

    @allure.title('Получение ошибки аутентификации курьера при вводе невалидных данных')
    @pytest.mark.parametrize('nonexistent_credentials', [
        {'login': create_random_login(), 'password': create_random_password()},
        Data.courier_data_with_wrong_password
    ])
    def test_courier_login_nonexistent_data_not_found(self, nonexistent_credentials):
        response = requests.post(Urls.URL_courier_login, data=nonexistent_credentials)
        expected_response = {
            'code': 404,
            'message': 'Учетная запись не найдена'
        }
        assert response.status_code == 404 and response.json() == expected_response

    @pytest.mark.parametrize('empty_credentials', [
        {'login': '', 'password': create_random_password()},
        {'login': Data.valid_login, 'password': ''}
    ])
    def test_courier_login_empty_credentials_bad_request(self, empty_credentials):
        response = requests.post(Urls.URL_courier_login, data=empty_credentials)
        expected_response = {
            'code': 400,
            'message': 'Недостаточно данных для входа'
        }
        assert response.status_code == 400 and response.json() == expected_response