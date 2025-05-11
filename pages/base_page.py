from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException

class BasePage:
    def __init__(self, browser : Chrome, url : str, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self): 
        self.browser.get(self.url)

    def is_element_present(self, how : str, what: str):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
