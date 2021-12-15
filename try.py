import math
from time import sleep

from behave import given, then, use_step_matcher, step
import sys

from functions.support_functions.webdriver_actions import by_css
from functions.support_functions.support import factorialtest

use_step_matcher("re")


@given("UI: I am on factorial calculator page")
def check_login_page(context):
    try:
        context.browser.get('https://cameramatics.pythonanywhere.com/')
        sleep(10)
        title_text = context.browser.title()
        if "Factorial" == title_text:
            pass
        else:
            sys.exit(1)
    except Exception as e:
        context.exc = e


@given(u'UI: Input an integer 5')
def step_impl(context):
    text_input_field = by_css(context, 'input#number')
    text_input_field.click()
    text_input_field.clear()
    text_input_field.send_keys('5')
    sleep(5)


@given(u'UI: Click Calculate')
def click_calculate(context):
    button_calculate = by_css(context, 'button#getFactorial')
    button_calculate.click()
    sleep(5)


@step('Verify the factorial of (?P<value>.+) is (?P<result>.+)')
def verify_result(context, value, result):
    ui_result = by_css(context, 'p#resultDiv')
    factorial_value = factorialtest(value)

    assert result in ui_result.text
    assert str(factorial_value) in ui_result.text


