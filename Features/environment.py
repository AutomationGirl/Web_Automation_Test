from selenium import webdriver
import os


def before_all(context):
    path = "/Users/hr6651/PycharmProjects/Flipkart_Automation/driver/chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = path
    driver = webdriver.Chrome(path)
    driver.implicitly_wait(20)
    driver.maximize_window()
    context.driver = driver


def after_all(context):
    context.driver.quit()

