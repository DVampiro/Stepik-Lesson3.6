import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru, en, es, fr")
    parser.addoption('--pause', action='store', default=0,
                     help="Включение паузы после загрузки")


# Включение паузы через командную строку
@pytest.fixture(scope="function")
def pause_time(request):
    pause_mode = request.config.getoption("pause")
    return pause_mode


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    options = webdriver.ChromeOptions()
    user_language = request.config.getoption("language")
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language})

    # Для отключения всяких сообщений DevTools. Надоели.
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
