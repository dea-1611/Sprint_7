class Data:
    valid_login = 'Max1994'
    valid_password = 'qwerty'
    valid_firstname = 'Max'
    valid_courier_data = {'login': 'Max1994', 'password': 'qwerty', 'firstName': 'Max'}
    courier_data_without_name = {'login': 'Max1994', 'password': '1234'}
    courier_data_with_wrong_password = {'login': 'Max1994', 'password': '123456'}
    courier_data_missing_fields = {'login': 'test_login'}

class ErrorMessages:
    LOGIN_EXISTS = 'Этот логин уже используется. Попробуйте другой.'
    ACCOUNT_NOT_FOUND = 'Учетная запись не найдена'
    NOT_ENOUGH_DATA_FOR_LOGIN = 'Недостаточно данных для входа'
    NOT_ENOUGH_DATA_FOR_CREATE = 'Недостаточно данных для создания учетной записи'
    GATEWAY_TIMEOUT = 'Время ожидания ответа истекло'


class OrderData:
    order_data_grey_1 = {
        'firstName': 'Ифан',
        'lastName': 'бенМезд',
        'address': 'Дрифтвудский проспект, 18',
        'metroStation': 8,
        'phone': '+71234567890',
        'rentTime': 3,
        'deliveryDate': '2025-08-20',
        'comment': 'Когда-то я был крестоносцем Божественного Ордена.',
        'color': [
            'GREY'
        ]
    }

    order_data_black_2 = {
        'firstName': 'Себилла',
        'lastName': 'Калеран',
        'address': 'Лесная улица, 20',
        'metroStation': 10,
        'phone': '+70987654321',
        'rentTime': 7,
        'deliveryDate': '2025-08-25',
        'comment': 'Я разорвала свои оковы.',
        'color': [
            'BLACK'
        ]
    }

    order_data_two_colors_3 = {
        'firstName': 'Лоусе',
        'lastName': 'Бардова',
        'address': 'Клиника доктора Дэвы',
        'metroStation': 15,
        'phone': '+70000000000',
        'rentTime': 1,
        'deliveryDate': '2025-08-30',
        'comment': 'Всю свою жизнь я была артисткой',
        'color': [
            'BLACK', 'GREY'
        ]
    }

    order_data_no_colors_4 = {
        'firstName': 'Константин',
        'lastName': 'Фейн',
        'address': 'Вечная улица, 8',
        'metroStation': 20,
        'phone': '+78888888888',
        'rentTime': 2,
        'deliveryDate': '2025-08-08',
        'comment': 'Глупые смертные',
        'color': []
    }

