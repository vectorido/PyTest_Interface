from selenium.webdriver.common.by import By


def test_assert_button_presence(browser):
    browser.get(f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    browser.implicitly_wait(10)

    basket_button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-lg.btn-add-to-basket')

    assert basket_button
