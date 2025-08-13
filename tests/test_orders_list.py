import requests
import allure
import pytest
from ..urls import Urls


class TestOrdersListGet:

    @allure.title('Получение списка заказов')
    def test_orders_list_get_success(self):
        response = requests.get(Urls.URL_orders_create)
        assert type(response.json()['orders']) == list and 'id' in response.json()['orders'][0]