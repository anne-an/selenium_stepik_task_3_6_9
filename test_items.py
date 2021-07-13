import time


def test_add_to_cart_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(10)
    add_button = browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
    assert add_button is not None
