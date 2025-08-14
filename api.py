import requests
from allure_commons.types import AttachmentType
import allure
from .urls import URL_COURIER_CREATE, URL_COURIER_LOGIN, URL_COURIER_DELETE, URL_ORDERS_CREATE, URL_ORDERS_LIST

class CourierAPI:
    @staticmethod
    @allure.step('Создание курьера')
    def create_courier(data):
        return requests.post(URL_COURIER_CREATE, data=data)

    @staticmethod
    @allure.step('Авторизация курьера')
    def login_courier(data):
        return requests.post(URL_COURIER_LOGIN, data=data)

    @staticmethod
    @allure.step('Удаление курьера')
    def delete_courier(courier_id):
        return requests.delete(f"{URL_COURIER_DELETE}/{courier_id}")

class OrderAPI:
    @staticmethod
    @allure.step('Создание заказа')
    def create_order(data):
        return requests.post(URL_ORDERS_CREATE, json=data)

    @staticmethod
    @allure.step('Получение списка заказов')
    def get_orders_list():
        return requests.get(URL_ORDERS_LIST)
