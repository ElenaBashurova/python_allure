import pytest
from selene import browser



@pytest.fixture()
def browser_management_github():
    browser.config.base_url = 'https://github.com'
    browser.config.timeout = 2.0
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield
    browser.quit()