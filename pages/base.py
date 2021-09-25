import yaml
from os.path import join, dirname, abspath

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

locators_file = join(dirname(dirname(abspath(__file__))),
                "locators", "locators.yaml")

class Base(object):

    def __init__(self, driver):
        self.driver = driver
        with open(locators_file) as f:
            self.locators = yaml.load(f, Loader=yaml.FullLoader)

    def fill_form(selector, selector_value, value, timeout=5):
        webdriver = WebDriverWait(self.driver, timeout)
        if selector == 'id':
            elem = webdriver.until(EC.visibility_of_element_located(
                        (By.ID, selector_value)))
        elif selector == 'xpath':
            elem = webdriver.until(EC.visibility_of_element_located(
                        (By.XPATH, selector_value)))

    def click(selector, selector_value, value, timeout=5):
        webdriver = WebDriverWait(self.driver, timeout)
        if selector == 'id':
            elem = webdriver.until(EC.visibility_of_element_located(
                        (By.ID, selector_value)))
        elif selector == 'xpath':
            elem = webdriver.until(EC.visibility_of_element_located(
                        (By.XPATH, selector_value)))
        elem.click()
