from selenium.webdriver.common.by import By

from generic.base_driver import BaseDriver
from utilities.utils import Utils


class SearchFlightsResultsPage(BaseDriver):
    log = Utils.custom_logger()
    __filter_flights_by_one_stop = (By.XPATH, "//p[text()='1']")
    __filter_flights_by_two_stops = (By.XPATH, "//p[text()='2']")
    __filter_flights_by_non_stop = (By.XPATH, "//p[text()='0']")
    __all_stops = (By.XPATH, "//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop(s)')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_filter_flights_by_one_stop(self):
        return self.driver.find_element(*self.__filter_flights_by_one_stop)

    def get_filter_flights_by_two_stops(self):
        return self.driver.find_element(*self.__filter_flights_by_two_stops)

    def get_filter_flights_by_non_stop(self):
        return self.driver.find_element(*self.__filter_flights_by_non_stop)

    def filter_by_stop(self, by_stop):
        if by_stop == "1 Stop":
            self.get_filter_flights_by_one_stop().click()
            self.log.info("Selected flights with 1 Stop")
        elif by_stop == "2 Stop":
            self.get_filter_flights_by_two_stops().click()
            self.log.info("Selected flights with 2 Stops")
        elif by_stop == "Non Stop":
            self.get_filter_flights_by_non_stop().click()
            self.log.info("Selected Non Stop flights")
        else:
            self.log.info("Please provide valid filter option")

    def get_search_flights_results(self):
        return self.wait_until_presence_of_all_elements_located(*self.__all_stops)
