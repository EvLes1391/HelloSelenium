from selenium.webdriver.common.by import By
from .base_page import SeleniumBasePage
from selenium.webdriver.support import expected_conditions as EC

class GooglePage(SeleniumBasePage):
    SEARCH_INPUT = (By.NAME, 'q')
    SEARCH_BUTTON = (By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
    RESULTS = (By.CSS_SELECTOR, 'h3')

    def search(self, query):
        self.input_text(self.SEARCH_INPUT, query)
        self.click(self.SEARCH_BUTTON)
    
    def get_first_result_text(self):
        return self.wait_for_element(self.RESULTS).text
    
    def get_nth_result_text(self, n=1):
        results = self.wait.until(
            EC.visibility_of_all_elements_located(self.RESULTS)
        )
        return results[n-1].text if len(results) >= n else ""