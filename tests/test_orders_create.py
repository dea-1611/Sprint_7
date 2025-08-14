import allure
import pytest
from Sprint_7.data import OrderData
from Sprint_7.api import OrderAPI

class TestOrderCreation:
    @allure.title('Создание заказа с серым самокатом')
    @allure.step('Создание заказа с одним серым самокатом. Проверка кода и тела ответа.')
    def test_create_order_grey(self):
        response = OrderAPI.create_order(OrderData.order_data_grey_1)
        assert response.status_code == 201
        assert 'track' in response.json()

    @allure.title('Создание заказа с черным самокатом')
    @allure.step('Создание заказа с одним черным самокатом. Проверка кода и тела ответа.')
    def test_create_order_black(self):
        response = OrderAPI.create_order(OrderData.order_data_black_2)
        assert response.status_code == 201
        assert 'track' in response.json()

    @allure.title('Создание заказа с двумя цветами')
    @allure.step('Создание заказа с двумя цветами самоката. Проверка кода и тела ответа.')
    def test_create_order_two_colors(self):
        response = OrderAPI.create_order(OrderData.order_data_two_colors_3)
        assert response.status_code == 201
        assert 'track' in response.json()

    @allure.title('Создание заказа без указания цвета')
    @allure.step('Создание заказа без указания цвета самоката. Проверка кода и тела ответа.')
    def test_create_order_no_colors(self):
        response = OrderAPI.create_order(OrderData.order_data_no_colors_4)
        assert response.status_code == 201
        assert 'track' in response.json()

