from abc import ABC, abstractmethod
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(ABC):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    @abstractmethod
    def input_text(self, locator, text):
        pass

    @abstractmethod
    def click(self, locator):
        pass

    def wait_for_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def get_title(self):
        return self.driver.title
    

class SeleniumBasePage(BasePage):
    def input_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)
    
    def click(self, locator):
        self.wait_for_element(locator).click()

# Для будущей поддержки PlayWright
class PlaywrightBasePage(BasePage):
    # Методы для Playwright
    pass