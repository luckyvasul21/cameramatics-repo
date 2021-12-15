#!/usr/bin/env python -u

import os

from selenium import webdriver
from selenium.common.exceptions import WebDriverException

global env, working_folder, application

working_folder = os.getcwd()

print('working folder:'+os.getcwd())

# BEHAVE_DEBUG_ON_ERROR = False
#
# def setup_debug_on_error(userdata):
#     global BEHAVE_DEBUG_ON_ERROR
#     BEHAVE_DEBUG_ON_ERROR = userdata.getbool("BEHAVE_DEBUG_ON_ERROR")


def before_all(context):
    try:

        print("initiating chrome driver")

        options = webdriver.ChromeOptions()
        options.add_argument('start-maximized')

        prefs = {'profile.default_content_setting_values.automatic_downloads': 1,
                 'download.prompt_for_download': False,
                 'download.default_directory': working_folder+"\\test_results\downloads", # IMPORTANT - ENDING SLASH V IMPORTANT
                 }

        options.add_experimental_option("prefs", prefs)

        chrome_driver_path = working_folder+'\shared_resources\chromedriver.exe'
        context.browser = webdriver.Chrome(chrome_options=options, executable_path=chrome_driver_path)
    except Exception:
        print(Exception)
        context.browser.quit()


def after_all(context):
    context.browser.quit()
    # os.system("taskkill /f /im chromedriver.exe")
