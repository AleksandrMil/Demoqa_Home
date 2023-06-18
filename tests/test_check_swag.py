from pages.swag_labs import SwagLabs


def test_swag_exist(browser):
    swag_labs_page = SwagLabs(browser)
    swag_labs_page.visit()

    assert swag_labs_page.exist_logo()
    assert swag_labs_page.exist_username()
    assert swag_labs_page.exist_password()
