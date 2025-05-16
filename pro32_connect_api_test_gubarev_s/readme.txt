Команда для запуска теста
pytest tests/test_update_user_name.py -v -s

Команда для запуска теста с формированием отчета Allure
python -m pytest -s -v --alluredir=allure-results tests\test_update_user_name.py -v -s

Запустить сервер Allure в браузере
allure serve allure-results/