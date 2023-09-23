from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from selenium import webdriver

from pages.drag_drop import dragdrop


def before_scenario(context,scenario):
    context.browser = webdriver.Chrome()
    context.browser.set_window_position(0, 0)  # NOTE: 0,0 might fail on some systems
    context.browser.set_window_size(800, 600)
    context.dd=dragdrop(context.browser)

def after_scenario(context,scenario):
    context.browser.close()

def after_step(context, step):
    if step.status=="failed":
        attach(
            context.browser.get_screenshot_as_png(),
            name="screenshot",
            attachment_type=AttachmentType.PNG
        )