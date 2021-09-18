from selenium import webdriver


def test():
    url = "https://plugins.jenkins.io/shiningpanda"
    path = "C:/chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.implicitly_wait(5)
    driver.get(url)
    title = driver.find_element_by_xpath('//*[@id="grid-box"]/div[1]/h1').text
    assert "ShiningPanda" == title
    driver.quit()
