import pytest
import requests
from utils.constants import *
from dotenv import load_dotenv
import os
import allure


@pytest.fixture(scope='session', autouse=True)
def settings_tests():
    """Фикстура для обозначения начала и окончания теста."""
    print("\n * НАЧАЛО ТЕСТА *")
    yield
    print("\n * КОНЕЦ ТЕСТА *")


@pytest.fixture(scope="module")
def session_and_llt():
    """Фикстура для создания сессии и получения llt cookie."""

    load_dotenv()
    credentials = {
        'login': os.getenv("LOGIN"),
        'password': os.getenv("PASSWORD")
    }

    session = requests.Session()

    with allure.step('Вход в личный кабинет'):
        print("\n- Вход в личный кабинет - ")

        response = session.post(LOGIN_URL, headers=headers, data=credentials)

        assert response.status_code == 200, f"Ошибка входа: {response.text}"
        print(f"[{response.status_code}] {response.url}")
        print(response.json())

    with allure.step('Сохранение аутентификационной cookie "llt"'):
        print("\n- Сохранение аутентификационной cookie 'llt' - ")
        cookies = session.cookies.get_dict()
        llt_cookie = cookies.get('llt')
        assert llt_cookie is not None, "Cookie 'llt' не найдена"
        print(f" Найдена cookie 'llt': {llt_cookie}")

        return session, llt_cookie
