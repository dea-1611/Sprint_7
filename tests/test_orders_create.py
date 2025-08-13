import requests
import allure
import pytest
from ..data import OrderData
from ..urls import URL_ORDERS_CREATE

class TestOrderCreation:
    @allure.title('Создание заказа с серым самокатом')
    def test_create_order_grey(self):
        response = requests.post(URL_ORDERS_CREATE, json=OrderData.order_data_grey_1)
        assert response.status_code == 201
        assert 'track' in response.json()

    @allure.title('Создание заказа с черным самокатом')
    def test_create_order_black(self):
        response = requests.post(URL_ORDERS_CREATE, json=OrderData.order_data_black_2)
        assert response.status_code == 201
        assert 'track' in response.json()

    @allure.title('Создание заказа с двумя цветами')
    def test_create_order_two_colors(self):
        response = requests.post(URL_ORDERS_CREATE, json=OrderData.order_data_two_colors_3)
        assert response.status_code == 201
        assert 'track' in response.json()

    @allure.title('Создание заказа без указания цвета')
    def test_create_order_no_colors(self):
        response = requests.post(URL_ORDERS_CREATE, json=OrderData.order_data_no_colors_4)
        assert response.status_code == 201
        assert 'track' in response.json()
