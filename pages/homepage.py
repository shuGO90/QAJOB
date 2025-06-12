from selenium.webdriver.common.by import  By
import time
class HomePage:
    def __init__(self, browser):
       self.browser = browser

    def open(self):
        self.browser.get('https://dev.demoblaze.com/#')

    def click_galaxy_s6(self):
        galaxy_s6 = self.browser.find_element(By.XPATH, value='//a[text()="Samsung galaxy s6"]')
        galaxy_s6.click()

    def click_monitor(self):
       monitor_link = self.browser.find_element(By.CSS_SELECTOR, value='a.list-group-item:nth-child(4)')
       monitor_link.click()


    def check_products_count(self, count):
        monitors = self.browser.find_elements(By.CSS_SELECTOR, '.card')
        time.sleep(3)
        assert len(monitors) == 2

