import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome("chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://plugins.jenkins.io/shiningpanda")
    yield driver
    driver.quit()


def test_check(browser):
    title = browser.find_elements_by_xpath('//*[@id="grid-box"]/div[1]')
    text = "ShiningPanda"
    assert text != title
    browser.quit()
