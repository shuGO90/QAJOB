from pages.homepage import HomePage
from pages.product import ProductPage
import time


def test_open_s6(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(browser)
    product_page.chek_title_is('Samsung galaxy s6')



def test_two_monitors(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_monitor()
    time.sleep(3)
    homepage.check_products_count(2)