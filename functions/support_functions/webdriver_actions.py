import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#------------------------------------------------------------------------------------
timeout = 10


def by_xpath(context, locator):
    try:
        # wait = ui.WebDriverWait(context.browser, timeout)
        # element = wait.until(lambda browser: browser.find_element_by_xpath(locator))
        element = ui.WebDriverWait(context.browser, timeout).until(EC.presence_of_element_located((By.XPATH, locator)))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print('\nElement {} not found'.format(locator))


def by_id(context, locator):
    try:
        # wait = ui.WebDriverWait(context.browser, timeout)
        # element = wait.until(lambda browser: browser.find_element_by_id(locator))
        element = ui.WebDriverWait(context.browser, timeout).until(EC.presence_of_element_located((By.ID, locator)))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print('\nElement {} not found'.format(locator))


def by_element(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(lambda browser: browser.find_element(locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print('\nElement {} not found'.format(locator))

def by_text(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(lambda browser: browser.find_element_by_link_text(locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print('\nElement {} not found'.format(locator))

def by_part_text(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(lambda browser: browser.find_element_by_partial_link_text(locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print('\nElement {} not found'.format(locator))


def by_tag(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(lambda browser: browser.find_element_by_tag_name(locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print('\nElement {} not found'.format(locator))


def by_name(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(lambda browser: browser.find_element_by_name(locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print('\nElement {} not found'.format(locator))

def by_css(context, locator):
    try:
        # wait = ui.WebDriverWait(context.browser, timeout)
        # element = wait.until(lambda browser: browser.find_element_by_css_selector(locator))
        element = ui.WebDriverWait(context.browser, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print('\nElement {} not found'.format(locator))

def by_class(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(lambda browser: browser.find_element_by_class_name(locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print('\nElement {} not found'.format(locator))

#=============================================================================================
def all_by_id(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(lambda browser: browser.find_elements_by_id(locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print('\nElement {} not found'.format(locator))

def all_by_xpath(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(lambda browser: browser.find_elements_by_xpath(locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print('\nElement {} not found'.format(locator))

def all_by_element(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(lambda browser: browser.find_elements(locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print('\nElement {} not found'.format(locator))

def all_by_text(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(lambda browser: browser.find_elements_by_link_text(locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print('\nElement {} not found'.format(locator))

def all_by_part_text(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(lambda browser: browser.find_elements_by_partial_link_text(locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print('\nElement {} not found'.format(locator))

def all_by_tag(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(lambda browser: browser.find_elements_by_tag_name(locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print('\nElement {} not found'.format(locator))


def all_by_name(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(lambda browser: browser.find_elements_by_name(locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print('\nElement {} not found'.format(locator))

def all_by_css(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(lambda browser: browser.find_elements_by_css_selector(locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print('\nElement {} not found'.format(locator))

def all_by_class(context, locator):
    try:
        wait = ui.WebDriverWait(context.browser, timeout)
        element = wait.until(lambda browser: browser.find_elements_by_class_name(locator))
        context.exc = None
        return element
    except Exception as e:
        context.exc = e
        print('\nElement {} not found'.format(locator))



