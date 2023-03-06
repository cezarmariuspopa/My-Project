import unittest
from time import sleep
import random
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Emag(unittest.TestCase):

    SEARCH_PRODUCT = (By.ID, "searchboxTrigger")
    PRESS_SEARCH = (By.XPATH, '//i[@class="em em-search"]')
    SELECT_PRODUCT = (By.CLASS_NAME, 'card-v2-thumb-inner')
    SELECT_SECOND_PRODUCT = (By.XPATH,'//*[@id="card_grid"]/div[2]/div[1]/div[1]/div[3]/a[1]/div[1]/img[1]')
    ADD_FIRST_PRODUCT_TO_CHART= (By.ID,'card_grid')
    ADD_SECOND_TO_CHART = (By.XPATH,'//*[@id="card_grid"]/div[2]/div[1]/div[1]/div[4]/div[2]/form[1]/button[1]')
    GO_TO_CHART = (By.ID, "my_cart")
    HOME_PAGE = (By.CLASS_NAME, "navbar-brand")


    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(15)
        self.chrome.get("https://www.emag.ro/")
        self.chrome.find_element(By.ID, "searchboxTrigger").send_keys("Laptopuri")
        self.chrome.find_element(*self.PRESS_SEARCH).click()

    def tearDown(self):
        self.chrome.quit()


    def test_search_product(self):
        actual_url = self.chrome.current_url
        self.chrome.find_element(*self.PRESS_SEARCH).click()


    def test_new_url(self):
        actual_url = self.chrome.current_url
        expected_url = 'https://www.emag.ro/search/Laptopuri?ref=effective_search'
        assert actual_url == expected_url, 'wrong url'

    def test_laptopuri_is_displayed(self):
        actual_text = self.chrome.find_element(By.XPATH, '//*[@id="main-container"]/section[1]/div/div[3]/div[2]/div[1]/div[1]/div/span/span[2]').text
        expected_text = '"Laptopuri"'
        self.assertEqual(actual_text,expected_text, "Displayed wrong text")


    def test_page_title(self):
        self.chrome.current_url
        actual_title = self.chrome.title
        expected_title = 'Cauți Laptopuri? Alege din oferta eMAG.ro'
        assert actual_title == expected_title, "Wrong title returned"

    def test_select_first_product(self):
        self.chrome.current_url
        self.chrome.find_element(*self.SELECT_PRODUCT).click()


    def test_add_first_product_to_chart(self):
        self.chrome.current_url
        self.chrome.find_element(*self.ADD_FIRST_PRODUCT_TO_CHART).click()

    def test_select_second_product(self):
        self.chrome.current_url
        self.chrome.find_element(*self.SELECT_SECOND_PRODUCT).click()

    def test_add_second_product_to_chart(self):
        self.chrome.current_url
        self.chrome.find_element(*self.ADD_SECOND_TO_CHART).click()
        sleep(5)

    def test_go_to_chart(self):
        self.chrome.current_url
        self.chrome.find_element(*self.GO_TO_CHART).click()


    def test_return_home_page(self):
        self.chrome.current_url
        self.chrome.find_element(*self.HOME_PAGE).click()
