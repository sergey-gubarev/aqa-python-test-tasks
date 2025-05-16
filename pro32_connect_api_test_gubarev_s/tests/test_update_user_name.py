from faker import Faker
from utils.constants import *
import pytest
import allure

fake = Faker(['ru_RU', 'en_US'])


@pytest.mark.medium
@allure.feature('Взаимодействие с данными пользователя')
@allure.story('Post')
@allure.title('Изменение имени и фамилии пользователя')
def test_update_user_name(session_and_llt):
    session, llt_cookie = session_and_llt

    new_name = fake.first_name()
    new_surname = fake.last_name()

    with allure.step('Изменение имени и фамилии пользователя'):
        print("\n- Изменение имени и фамилии пользователя - ")

        json_data = {
            'ad_allowed': False,
            'beta': False,
            'country': 'ru',
            'dateformat': 0,
            'language': 'ru',
            'name': new_name,
            'surname': new_surname,
            'timezone': 0,
        }

        response_update = session.post(PROFILE_UPDATE_URL, headers=headers, json=json_data, cookies={'llt': llt_cookie})

        assert response_update.status_code == 200, f"Ошибка обновления профиля: {response_update.text}"
        print(f"[{response_update.status_code}] {response_update.url}")
        print(response_update.json())

    with allure.step('Проверка, что данные пользователя изменились'):
        print("\n- Проверка, что данные пользователя изменились - ")

        response_profile = session.get(PROFILE_INFO_URL, headers=headers, cookies={'llt': llt_cookie})

        assert response_profile.status_code == 200, f"Не удалось получить данные профиля: {response_profile.text}"

        profile_data = response_profile.json()
        current_name = profile_data.get('name')
        current_surname = profile_data.get('surname')

        print(f"Получено имя: {current_name}, фамилия: {current_surname}")
        print(f"Ожидаемое имя: {new_name}, фамилия: {new_surname}")

        assert current_name == new_name and current_surname == new_surname, \
            "Имя или фамилия не были изменены корректно"

    print("\n -- Все шаги успешно выполнены --")
