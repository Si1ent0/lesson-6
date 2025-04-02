from datetime import time
from pprint import pprint


def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    current_time = time(hour=3)

    is_dark_theme = current_time >= time(hour=22) or current_time <= time(6)
    assert is_dark_theme is True

def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """
    current_time = time(hour=16)
    dark_theme_enabled_by_user = True

    auto_time_theme = current_time >= time(hour=22) or current_time <= time(6)
    print(auto_time_theme)
    is_dark_theme =  auto_time_theme or dark_theme_enabled_by_user
    assert is_dark_theme is True

def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    def get_user_olga():
        for user in users:
            if user["name"] == "Olga":
                olga = user
                return olga

    suitable_users = get_user_olga()
    assert suitable_users == {"name": "Olga", "age": 45}

    def get_young_users():
        young_users = []
        for user in users:
            if user["age"] < 20:
                young_users.append(user)
        return young_users

    suitable_users = get_young_users()
    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"


def print_name_function(func, *args, **kwargs):
    function_name = func.__name__.replace('_', ' ').title()
    arg = ",".join(args)
    result = f'{function_name} [{arg}]'
    return result

def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    actual_result = print_name_function(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = print_name_function(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = print_name_function(find_registration_button_on_login_page, page_url + ', ' +button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"

