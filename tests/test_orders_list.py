import allure
from Sprint_7.api import OrderAPI

class TestOrdersList:
    @allure.title('Получение списка заказов')
    @allure.step('Запрос списка всех заказов. Проверка кода и тела ответа.')
    def test_get_orders_list(self):
        response = OrderAPI.get_orders_list()
        assert response.status_code == 200
        assert 'orders' in response.json()
        assert isinstance(response.json()['orders'], list)

