from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.request_quote_form_page import RequestAQuoteForm


def test_negative_case():
    """Тест отправки формы с некорректными данными."""

    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--ignore-certificate-errors")
    options.add_experimental_option("detach", True)

    # Инициализация драйвера
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    form = RequestAQuoteForm(driver)

    try:
        # Открыть страницу
        form.open()

        # Прокрутить до формы
        form.scroll_to_form()

        # Заполнить форму некорректными данными
        form.fill_name("%&*")
        form.fill_email("invalid-email")
        form.fill_message("1234")

        # Проверка негативного сценария
        name_field_invalid = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@class='form-control bg-light border-0 is-invalid'])[1]"))
        )
        email_field_invalid = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@class='form-control bg-light border-0 is-invalid'])[1]"))
        )
        message_field_invalid = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//textarea[@class='form-control bg-light border-0 is-invalid']"))
        )

        # Проверка, что поля помечены как невалидные
        assert name_field_invalid.is_displayed(), "Поле 'Your Name' должно быть помечено как невалидное."
        assert email_field_invalid.is_displayed(), "Поле 'Your Email' должно быть помечено как невалидное."
        assert message_field_invalid.is_displayed(), "Поле 'Message' должно быть помечено как невалидное."

        submit_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-dark w-100 py-3']"))
        )
        # Тест упадет, так как кнопка отправки остается активна с некорректными данными
        assert not submit_button.is_enabled(), "Кнопка отправки формы должна быть неактивной при некорректных данных."


    finally:
        driver.quit()
