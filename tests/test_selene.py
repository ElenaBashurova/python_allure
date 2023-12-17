from selene.support.shared.jquery_style import s
from selene.support.shared import browser
from selene.support import by
from selene.support.conditions import be



def test_github_selene(browser_management_github):
    browser.open("/")

    s('.header-search-button').click()
    s('#query-builder-test').send_keys('ElenaBashurova/python_task').press_enter()
    s('[href="/ElenaBashurova/python_task"]').click()

    s('#issues-tab').click()
    s(by.partial_text("#1 opened")).should(be.visible)



