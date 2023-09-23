from selenium.webdriver import ActionChains
from behave import *
from selenium.webdriver.common.by import By



@given(u'the user Navigate to the URL https://qavbox.github.io/demo/dragndrop/')
def step_open(context):
    context.browser.get("https://qavbox.github.io/demo/dragndrop/")


@when(u'he drag and drop the grey square in the blue square')
def dragndrop(context):
   context.dd.drag()


@then(u'he sees a messge "Dropped!"')
def step_verify(context):
    context.dd.verify()
    assert "Dropped!"== context.dd.verify().text

