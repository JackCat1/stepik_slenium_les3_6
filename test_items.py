from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def found_element_by_selector(browser, selector):
    try:
        browser.find_element(By.CSS_SELECTOR, selector)
    except NoSuchElementException:
        return False
    return True


def test_guest_should_see_basket_add_btn(browser):
    browser.get(link)
    assert found_element_by_selector(browser, "#add_to_basket_form button[type='submit']"), 'Basket submit ' \
                                                                                            'button not found'
