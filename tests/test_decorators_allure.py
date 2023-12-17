import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "ElenaBashurova")
@allure.feature("Issues")
@allure.link("https://github.com", name="Test_steps")
@allure.story("Найти Issues")
@allure.step('Открываем страницу GitHub')
def test_decorator_steps(browser_management_github):
    open_page_main()
    find_repo()
    open_repo()
    open_issues()
    check_text()


@allure.step('Открываем страницу GitHub')
def open_page_main():
    browser.open("/")


@allure.step("Найти репозиторий")
def find_repo():
    s(".header-search-button").click()
    s("#query-builder-test").type("ElenaBashurova/python_task")
    s("#query-builder-test").submit()


@allure.step('Открыть репозиторий')
def open_repo():
    s('[href="/ElenaBashurova/python_task"]').click()


@allure.step('Открыть Issues')
def open_issues():
    s('#issues-tab').click()


@allure.step('Проверить текст')
def check_text():
    s(by.partial_text("#1 opened")).should(be.visible)
