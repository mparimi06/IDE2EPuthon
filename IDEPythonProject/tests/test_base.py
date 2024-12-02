import pandas as pd
import pytest
import os
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class TestBase:

    @pytest.fixture(autouse=True)
    def init_driver(self):
        self.url = "https://www.webuyanycar.com/"
        option = Options()
        option.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=option)
        print(self.url)
        self.driver.get(self.url)
        yield
        self.driver.quit()

    def extract_data(self):

        path = os.getcwd()
        if "tests" in path:
            path = os.path.dirname(os.getcwd())
        path = path + "\\data\\input"
        files = os.listdir(path)

        pattern = re.compile("[A-Z]{2}[0-9]{2} ?[A-Z]{3}")

        vehicleList = []
        # Iterating the Input folder to read more than 1 input files
        for i,f in enumerate(files):
            file_path = path+"\\"+f
            with open(file_path, "r") as file:
                car_input_data = file.read()
                vehicleList = vehicleList+pattern.findall(car_input_data)

        return vehicleList

    def read_output_data(self):
        path = os.getcwd()
        if "tests" in path:
            path = os.path.dirname(os.getcwd())
        path = path + "\\data\\car_output.txt"
        df = pd.read_csv(path)
        return df

