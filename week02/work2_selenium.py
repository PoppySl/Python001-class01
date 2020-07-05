from selenium import webdriver
import time


class ShiMoLoginForSelenium:
    def __init__(self, userName, passWord):
        self.userName = userName
        self.passWord = passWord
        self.url = 'https://shimo.im/login?from=home'

    def login(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        driver.find_element_by_name('mobileOrEmail').send_keys(self.userName)
        driver.find_element_by_name('password').send_keys(self.passWord)
        driver.find_element_by_xpath(
            '//button[@class="sm-button submit sc-1n784rm-0 bcuuIb"]').click()
        time.sleep(5)
        print(driver.current_url)
        driver.close()


if __name__ == '__main__':
    userName = 'test'
    passWorld = 'test'
    ShiMoLoginForSelenium(userName, passWorld).login()
