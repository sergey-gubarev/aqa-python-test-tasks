import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import datetime


class RequestAQuoteForm:
    """ Класс содержащий локаторы и методы для главной страницы """

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://qatest.datasub.com/"

    def get_screenshot(self):
        """"Создание скриншота"""
        # Время пк ,а не utc date_now = datetime.now().strftime("%Y.%m.%d %H.%M.%S")
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot(
            f'screenshot/' + name_screenshot)
        print('Screenshot: ' + name_screenshot)

    def scroll_to_form(self):
        """Прокрутка страницы до формы 'Request A Quote'."""
        form_element = self.driver.find_element(By.XPATH, "//div[@class='bg-primary rounded h-100 d-flex "
                                                          "align-items-center p-5 wow zoomIn']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", form_element)
        self.get_screenshot()
        time.sleep(1)

    def open(self):
        """Открыть страницу с формой."""
        self.driver.get(self.url)
        self.get_screenshot()

    def fill_name(self, name):
        """Заполнить поле 'Your Name'."""

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "name"))).send_keys(name)
        self.get_screenshot()

    def fill_email(self, email):
        """Заполнить поле 'Your Email'."""
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "email"))).send_keys(email)
        self.get_screenshot()

    def select_service(self, service):
        """Выбрать сервис из выпадающего списка."""
        dropdown = self.driver.find_element(By.ID, "service")
        dropdown.click()
        option = self.driver.find_element(By.XPATH, f"//option[text()='{service}']")
        option.click()
        self.get_screenshot()

    def select_account_purpose(self, purpose):
        """Выбрать радиокнопку 'Account Purpose'."""
        radio_button = self.driver.find_element(By.XPATH, f"//input[@value='{purpose}']")
        radio_button.click()
        self.get_screenshot()

    def select_withdrawal_options(self, options):
        """Выбрать чекбоксы 'Withdrawal Option'."""
        for option in options:
            checkbox = self.driver.find_element(By.XPATH, f"//input[@value='{option}']")
            checkbox.click()
            self.get_screenshot()

    def fill_message(self, message):
        """Заполнить поле 'Message'."""
        self.driver.find_element(By.ID, "message").send_keys(message)
        self.get_screenshot()

    def submit_form(self):
        """Отправить форму."""
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-dark w-100 py-3']"))).click()
        self.get_screenshot()

    def get_success_message(self):
        """
        Получить сообщение об успешной отправке.
        Если текст не найден, выводится сообщение об ошибке.
        """
        try:
            success_message_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[text()='Форма отправлена.']"))
            )
            self.get_screenshot()
            if success_message_element.text.strip():
                return success_message_element.text
            else:
                print("Текст сообщения пустой.")
                return None

        except TimeoutException:
            print("Ошибка, отправка формы не произошла !.")
            self.get_screenshot()
            return None
