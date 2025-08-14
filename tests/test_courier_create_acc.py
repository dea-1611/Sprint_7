import allure
import pytest
from Sprint_7.data import Data, ErrorMessages
from Sprint_7.api import CourierAPI

class TestCourierCreation:
    @allure.title('Успешное создание курьера')
    @allure.step('Создание курьера с валидными данными. Проверка кода и тела ответа.')
    def test_create_courier_success(self, random_courier):
        response = CourierAPI.create_courier(random_courier)
        assert response.status_code == 201
        assert response.json() == {'ok': True}

    @allure.title('Создание дубликата курьера')
    @allure.step('Попытка создания курьера с существующим логином. Проверка кода и тела ответа.')
    def test_create_duplicate_courier(self):
        response = CourierAPI.create_courier(Data.valid_courier_data)
        assert response.status_code == 409
        assert response.json()['message'] == ErrorMessages.LOGIN_EXISTS

    @allure.title('Создание курьера без обязательных полей')
    @allure.step('Попытка создания курьера с пустыми полями. Проверка кода и тела ответа.')
    def test_create_courier_missing_fields(self):
        response = CourierAPI.create_courier({'login': 'test_login'})
        assert response.status_code == 400
        assert response.json()['message'] == ErrorMessages.NOT_ENOUGH_DATA_FOR_CREATE


