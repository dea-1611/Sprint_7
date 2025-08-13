import requests
import allure
from ..urls import URL_ORDERS_LIST

class TestOrdersList:
    @allure.title('Получение списка заказов')
    def test_get_orders_list(self):
        response = requests.get(URL_ORDERS_LIST)
        assert response.status_code == 200
        assert 'orders' in response.json()
        assert isinstance(response.json()['orders'], list)
