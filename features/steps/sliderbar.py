from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


@when(u'he move the slider bar')
def slidebar(context):
    context.dd.slider()


@then(u'the value 100 will be displayed')
def sliderverify(context):
    context.dd.verifyslider()