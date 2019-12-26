from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
url = "https://www.flipkart.com/"
testcase = TestCase()


class ProductSearch:

    def __init__(self, driver):
        self.driver = driver

    def open_application(self):
        self.driver.get(url)
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "_3Njdz7")))

    def click_on_cancel(self):
        if self.driver.find_element_by_xpath("/html/body/div[2]/div/div/button").is_displayed():
            self.driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()

    def search_product(self, product_name):
        search_item = self.driver.find_element_by_name("q")
        search_item.send_keys(product_name)
        search_item.submit()

    def verify_search_result(self, product_category):
        ui_text = self.driver.find_element_by_xpath('//a[contains(@href, "Footwear")]')
        testcase.assertEqual(ui_text.text, product_category, "category is not matching")

    def apply_filter(self):
        self.driver.execute_script(
            "document.querySelectorAll('input[placeholder=\"Search Brand\"]')[0].scrollIntoView()")
        self.driver.execute_script(
            "document.querySelectorAll('div[title=\"Nike\"] label')[0].click()")
        self.driver.execute_script(
            "document.querySelectorAll('div[title=\"Black\"] label')[0].click()")

    def verify_filter(self, b_name, c_name):
        self.driver.execute_script(
            "document.querySelectorAll('div[class=\"D0YrLF\"]')[0].scrollIntoView(true)")
        filter_name = self.driver.find_elements_by_xpath("//*[@id='container']/div/div[3]/div[2]/div/div[1]/div/div/div/section[1]/div[2]/div[1]/div/div[2]")
        for name in filter_name:
            if name == b_name:
                print("filter brand is {}".format(b_name))
            if name == c_name:
                print("filter colour is {}".format(c_name))

    def filter_result(self):
        product_count = self.driver.find_elements_by_xpath("//*[@id='container']/div/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[1]")
        testcase.assertEqual(len(product_count), 40, "product count are not matching")
        colour_code = self.driver.find_element_by_xpath("//*[@id='container']/div/div[3]/div[2]/div/div[2]/div/div/div/div/div/div[1]")
        colour = colour_code.value_of_css_property("color")
        actual_number = "rgba(135, 135, 135, 1)"
        testcase.assertEqual(colour, actual_number, "color is black")

    def product_details(self):
        self.driver.find_element_by_xpath("//*[@id='container']/div/div[3]/div[2]/div/div[2]/div[2]/div/div[1]/div/div/a[1]").click()

    def choose_product_size(self):
        self.switch_to_window()
        self.driver.execute_script("window.scrollTo(0, 200);")
        self.driver.find_element_by_xpath("//*[@id='swatch-0-size']/a").click()

    def click_on_buy_now(self):
        self.driver.find_element_by_class_name("_279WdV").click()

    def login_page(self):
        login_text = self.driver.find_element_by_xpath("//*[@id='container']/div/div[2]/div/div[1]/div[1]/div/h3/span[2]")
        testcase.assertEqual(login_text.text, "LOGIN OR SIGNUP", "login page is not open")

    def switch_to_window(self):
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)














