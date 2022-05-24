import time
from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    time.sleep(30)
    try:
        browser.find_element_by_css_selector('button.btn-add-to-basket')
    except NoSuchElementException:
        assert False, 'No button "Add to basket" on this page'