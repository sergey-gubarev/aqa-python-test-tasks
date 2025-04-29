from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.request_quote_form_page import RequestAQuoteForm


def test_positive_path():
    """Тест отправки формы с корректными данными."""

    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--ignore-certificate-errors")
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options,
                              service=ChromeService(ChromeDriverManager().install()))

    form = RequestAQuoteForm(driver)
    fake = Faker(['ru_RU', 'en_US'])

    fill_name_random = fake.bs()
    fill_message = fake.pystr(min_chars=6, max_chars=10)

    try:
        # Открыть страницу
        form.open()

        # Прокрутить до формы
        form.scroll_to_form()

        # Заполнить форму корректными данными
        form.fill_name(fill_name_random)
        form.fill_email("johndoe@example.com")
        form.select_service("Select A Service")  # Тест упадет, так как вариант "Select A Service"
        # в локаторе страницы помечен как не валидный
        form.select_account_purpose("Business")
        form.select_withdrawal_options(["Cash", "Card"])
        form.fill_message(fill_message)

        # Отправить форму
        form.submit_form()

        # Проверить сообщение об успешной отправке
        success_message = form.get_success_message()
        assert success_message == "Форма отправлена.", "Ошибка отправки формы. Проверьте корректность введенных данных"

    finally:
        driver.quit()
