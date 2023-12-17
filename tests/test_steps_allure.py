import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_steps(browser_management_github):
    with allure.step('Открываем страницу GitHub'):
        browser.open("/")

    with allure.step('Найти репозиторий'):
        s('.header-search-button').click()
        s('#query-builder-test').send_keys('ElenaBashurova/python_task').press_enter()

    with allure.step('Открыть репозиторий'):
        s('[href="/ElenaBashurova/python_task"]').click()

    with allure.step('Открыть Issues'):
        s('#issues-tab').click()

    with allure.step('Проверить текст'):
        s(by.partial_text("#1 opened")).should(be.visible)