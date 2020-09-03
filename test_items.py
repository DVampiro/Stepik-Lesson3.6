import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_select_language(browser, pause_select):
    browser.get(link)
    browser.implicitly_wait(5)  # На случай задержек
    button = browser.find_elements_by_class_name("btn-add-to-basket")
    assert len(button), "Кнопка не найдена!"

    lang = browser.find_element_by_css_selector(
        "[selected='selected']").text.strip()  # Получение активного языка

    print(f'Выбран язык: {lang}\nТекст на кнопке: {button[0].text}')

    if button[0].text == 'Ajouter au panier' or pause_select:
        if not pause_select:
            pause_select = 10  # Принудительное включение для французского
        print(f'Включена автопауза на {pause_select} секунд')
        time.sleep(int(pause_select))
