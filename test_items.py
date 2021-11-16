import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_items_to_basket(browser):
    browser.get(link)
    time.sleep(30)
    btn = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert btn.is_displayed()==True, "Кнопки нет на экране"