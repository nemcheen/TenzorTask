from pages.locators import Locators as loc
from pages.download_page import BasePage

URL = "https://sbis.ru"
URL_FOR_CHECK = 'https://tensor.ru/about'

def test_sbis(driver):
    page = BasePage(driver)
    page.driver.get(URL)
    page.wait_click(loc.contacts_loc)
    page.wait_click(loc.tenzor_banner)
    if len(driver.window_handles) > 1: # Check if more than 1 tab opened. If attribute <target='_blank'> in <a> element present
        driver.switch_to.window(driver.window_handles[-1]) # Switch to last opened tab
    element = page.wait_and_find(loc.power_in_human_block)
    assert element, "No 'Power in Human' block"
    page.wait_click(loc.about_link)
    assert page.check_url(URL_FOR_CHECK), "Page https://tensor.ru/about not opened"
    page.wait(loc.work_block)
    images = page.driver.find_elements(*loc.image)
    str_of_sizes, is_img_same = page.check_images(images)
    assert is_img_same, f"\nImages have different sizes!\n{str_of_sizes}"
