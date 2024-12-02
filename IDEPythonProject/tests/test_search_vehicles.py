from pages.home_page import HomePage
from pages.valuation_page import ValuationPage
from tests.test_base import TestBase
import logging
import pandas as pd
import random

class TestSearchVehicles(TestBase):


    def test_search(self):
        status = "Pass"
        vehicleList = self.extract_data()
        print("Vehicle Reg numbers:")
        print(vehicleList)
        logging.info(vehicleList)
        output_data =  self.read_output_data()

        home_page = HomePage(self.driver)
        valuation_page = ValuationPage(self.driver)

        for v in vehicleList:
            home_page.open_car_valuation_page()
            randomMileage = random.randint(100,100000)
            print("Vehicle: " + v)
            print("Mileage: " + str(randomMileage))
            row = output_data.loc[output_data['VARIANT_REG'] == v.replace(" ","")]
            if row.empty:
                print(v + " Vehicle not found in output file ")
            else:

                valuation_page.search_vehicle(v.replace(" ",""),randomMileage)
                data_found = valuation_page.get_vehicle_data()
                #using try block to iterate throu all vehecle numbers even when assertin fail
                try:
                    assert row.iloc[0,0] == data_found["number"]
                    assert row.iloc[0,1] == data_found["make"]
                    assert row.iloc[0,2] == data_found["model"]
                    assert row.iloc[0,3] == int(data_found["year"])
                except AssertionError as e:
                    print(e)
                    status = "Fail"
            print("Verified for : " + v)
            self.driver.get(self.url)
        assert status == "Pass", "Vehicle details not found in search or is not same as in Output file!!"


