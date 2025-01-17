from pages.base_page import BasePage
from pages.locators import Locators as loc
from pages.utility import check_images

URL = "https://sbis.ru"
URL_FOR_CHECK = 'https://tensor.ru/about'
# url2 = 'https://tensor.ru/'
# url3 = 'https://tensor.ru/about'

def test_sbis(driver):
    page = BasePage(driver)
    page.driver.get(URL)
    page.wait_click(loc.contacts_loc)
    page.wait_click(loc.tenzor_banner)
    if len(driver.window_handles) > 1: # Check if more than 1 tab opened. If attribute <target='_blank'> in <a> element present
        driver.switch_to.window(driver.window_handles[-1]) # Switch to last opened tab
    element = page.wait_and_find(loc.power_in_human_block)
    assert element, "No 'Power in Human' block"
    page.wait_click(loc.more_link)
    assert page.check_url(URL_FOR_CHECK), "Page https://tensor.ru/about not opened"
    images = page.driver.find_elements(*loc.image)
    result = check_images(images)
    str_of_sizes = result[1]
    is_img_same = result[0]
    assert is_img_same, f"\nImages have different sizes!\n{str_of_sizes}"
