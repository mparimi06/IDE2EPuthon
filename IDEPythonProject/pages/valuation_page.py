from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ValuationPage(BasePage):
    VALUATION_INPUT = (By.NAME, "registrationNumber")
    MILEAGE_INPUT = (By.NAME, "mileage")
    GET_BUTTON = (By.XPATH,".//form[@id='mvtb-lookup-form']//button")
    VEHICLE_NUM_XPATH = (By.XPATH, ".//section[contains(@class,'rimary-section')]//div[contains(@class,'details-vrm ')]")
    VEHICLE_MODEL_XPATH = (By.XPATH, ".//section[contains(@class,'rimary-section')]//div[text()='Model:']/..//div[contains(@class,'value')]")
    VEHICLE_MAKE_XPATH = (By.XPATH, ".//section[contains(@class,'rimary-section')]//div[text()='Manufacturer:']/..//div[contains(@class,'value')]")
    VEHICLE_YEAR_XPATH = (By.XPATH, ".//section[contains(@class,'rimary-section')]//div[text()='Year:']/..//div[contains(@class,'value')]")

    def search_vehicle(self, reg_number,mileage):
        self.wait_and_sendkeys_element(self.VALUATION_INPUT, reg_number)
        self.wait_and_sendkeys_element(self.MILEAGE_INPUT, mileage)
        self.wait_and_click_element(self.GET_BUTTON)

    def get_vehicle_data(self):
        try:
            vehicle_num_found = self.wait_and_getText_element(self.VEHICLE_NUM_XPATH)
            vehicle_model_found = self.wait_and_getText_element(self.VEHICLE_MODEL_XPATH)
            vehicle_make_found = self.wait_and_getText_element(self.VEHICLE_MAKE_XPATH)
            vehicle_year_found = self.wait_and_getText_element(self.VEHICLE_YEAR_XPATH)
            data_found = {"number":vehicle_num_found, "model": vehicle_model_found, "make": vehicle_make_found, "year":vehicle_year_found }
        except:
            print("Vehicle details not found in search")
            data_found = {"number":"", "model": "", "make": "", "year": ""}
        return data_found


