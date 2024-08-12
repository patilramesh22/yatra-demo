from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    def page_scroll(self):
        page_length = self.driver.execute_script(
            "window.scrollTo(0,document.body.scrollHeight);var page_length=document.body.scrollHeight;return page_length")
        match = False
        while match == False:
            last_count = page_length
            page_length = "window.scrollTo(0,document.body.scrollHeight);var page_length=document.body.scrollHeight;return page_length"
            if last_count == page_length:
                match = True

    def wait_until_element_is_clickable(self, locator, value):

        wait = WebDriverWait(self.driver,15)
        element=wait.until(EC.element_to_be_clickable((locator, value)))
        return element

    def wait_until_presence_of_all_elements_located(self, locator, value):
        wait = WebDriverWait(self.driver, 15)
        elements=wait.until(EC.presence_of_all_elements_located((locator, value)))
        return elements
