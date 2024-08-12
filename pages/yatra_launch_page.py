import time

from selenium.webdriver.common.by import By

from generic.base_driver import BaseDriver
from pages.search_flights_results_page import SearchFlightsResultsPage
from utilities.utils import Utils


class LaunchPage(BaseDriver):
    log = Utils.custom_logger()
    __dept_from = (By.ID, "BE_flight_origin_city")
    __search_results = (By.XPATH, "//div[@class='viewport']//li")
    __going_to = (By.ID, "BE_flight_arrival_city")
    __dept_date = (By.ID, "BE_flight_origin_date")
    __all_dates = (By.XPATH, "//div[@id='monthWrapper']//td[@class!='inActiveTD' and @class!='inActiveTD weekend']")
    __search_flights_btn = (By.XPATH, "//input[@value='Search Flights']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_dept_from_field(self):
        return self.wait_until_element_is_clickable(*self.__dept_from)

    def get_search_results_list(self):
        return self.wait_until_presence_of_all_elements_located(*self.__search_results)

    def dept_from_loc(self, dept_from_loc):
        self.get_dept_from_field().click()
        self.get_dept_from_field().send_keys(dept_from_loc)
        search_results_list = self.get_search_results_list()
        self.log.info(len(search_results_list))
        for result in search_results_list:
            self.log.info(result.text)
            if dept_from_loc in result.text:
                result.click()
                break
        print('--------------------------------------------------')

    def get_going_to_field(self):
        return self.wait_until_element_is_clickable(*self.__going_to)

    def going_to_loc(self, going_to_loc):
        self.get_going_to_field().click()
        self.get_going_to_field().send_keys(going_to_loc)
        search_results_list = self.get_search_results_list()
        self.log.info(len(search_results_list))
        for result in search_results_list:
            self.log.info(result.text)
            if going_to_loc in result.text:
                result.click()
                break

        print('--------------------------------------------------')

    def get_dept_date_field(self):
        return self.wait_until_element_is_clickable(*self.__dept_date)

    def get_all_dates_list(self):
        return self.wait_until_presence_of_all_elements_located(*self.__all_dates)

    def select_dept_date(self, departure_date):
        self.get_dept_date_field().click()
        all_dates = self.get_all_dates_list()
        for date in all_dates:
            if date.get_attribute("data-date") == departure_date:
                date.click()
                time.sleep(3)
                break

    def click_on_search_flights(self):
        self.driver.find_element(*self.__search_flights_btn).click()

    def search_flights(self, dept_from_loc, going_to_loc, departure_date):
        self.dept_from_loc(dept_from_loc)
        self.going_to_loc(going_to_loc)
        self.select_dept_date(departure_date)
        self.click_on_search_flights()
        search_flights_results = SearchFlightsResultsPage(self.driver)
        return search_flights_results
