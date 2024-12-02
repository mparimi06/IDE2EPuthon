from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver):
        self.driver = driver


    def find_element(self, element_path):
       return self.driver.find_element(*element_path)

    def wait_and_find_element(self, element_path):
        return WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(element_path))

    def wait_and_click_element(self, element_path):
        ele = WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(element_path))
        ele.click()

    def wait_and_sendkeys_element(self, element_path, input_text):
        ele = WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(element_path))
        ele.clear()
        ele.send_keys(input_text)

    def wait_and_getText_element(self, element_path):
        ele = WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(element_path))
        return ele.text

