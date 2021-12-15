from selenium import webdriver
from selenium.common.exceptions import WebDriverException

import os


class Browser(object):

    try:
        if (object == 'chrome'):
            chrome_path = os.getcwd()+'/resources/chromedriver.exe'
            options = webdriver.ChromeOptions()
            # options.add_argument('headless')
            #    options.add_argument('disable-gpu')
            options.add_argument('start-maximized')
            driver = webdriver.Chrome(chrome_path, chrome_options=options)

            driver.implicitly_wait(30)
            driver.set_page_load_timeout(30)
    except WebDriverException:
        driver.quit()
