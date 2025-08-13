import requests
import allure
import pytest
from ..data import Data
from ..urls import URL_COURIER_LOGIN, URL_COURIER_CREATE, URL_COURIER_DELETE
from ..helpers import create_random_login, create_random_password, create_random_firstname


class TestCourierLogin:
    @allure.title('Успешная аутентификация курьера')
    def test_courier_login_success(self):
        response = requests.post(URL_COURIER_LOGIN, data={
            'login': Data.valid_login,
            'password': Data.valid_password
        })
        assert response.status_code == 200
        assert 'id' in response.json()

    @allure.title('Аутентификация с неверными данными')
    @pytest.mark.parametrize('invalid_data', [
        {'login': create_random_login(), 'password': create_random_password()},
        Data.courier_data_with_wrong_password
    ])
    def test_courier_login_invalid_credentials(self, invalid_data):
        response = requests.post(URL_COURIER_LOGIN, data=invalid_data)
        assert response.status_code == 404
        assert response.json()['message'] == 'Учетная запись не найдена'

    @allure.title('Аутентификация без обязательных полей')
    @pytest.mark.parametrize('missing_field', ['login', 'password'])
    def test_courier_login_missing_fields(self, missing_field):
        credentials = {
            'login': Data.valid_login,
            'password': Data.valid_password
        }
        del credentials[missing_field]

        response = requests.post(URL_COURIER_LOGIN, data=credentials)

        assert response.status_code in [400, 504]
        if response.status_code == 400:
            assert response.json()['message'] == 'Недостаточно данных для входа'
