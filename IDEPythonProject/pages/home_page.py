from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    VALUATION_LINK = (By.XPATH, ".//li[contains(@class,'active')]//a[contains(@href,'car-valuation')]")
    COOKIES_BUTTON = (By.ID,"onetrust-accept-btn-handler")



    def open_car_valuation_page(self):
            try:
                self.wait_and_click_element(self.COOKIES_BUTTON)
            except:
                print("")

            self.wait_and_click_element(self.VALUATION_LINK)
