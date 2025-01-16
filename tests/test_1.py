from pages.base_page import BasePage
from pages.locators import Locators
from pages.utility import check_img

about_url = 'https://tensor.ru/about'
url1 = "https://sbis.ru"
url2 = 'https://tensor.ru/'
# url3 = 'https://tensor.ru/about'

def test_sbis(driver):
    contacts_page = BasePage(driver)
    contacts_page.driver.get(url1)
    contacts_page.wait_click(Locators.contacts_loc)
    contacts_page.wait_click(Locators.tenzor_banner)
    element = contacts_page.wait_and_find(Locators.power_in_human_block)
    assert element, "No 'Power in Human' block"

def test_tenzor(driver):
    next_page = BasePage(driver)
    next_page.driver.get(url2)
    next_page.wait_click(Locators.more_link)
    assert next_page.check_url(about_url), "Page https://tensor.ru/about not opened"
    parent_div = next_page.wait_and_find(Locators.parent_div_img)
    img_elements = parent_div.find_elements(*Locators.img)
    result = check_img(img_elements)
    assert result[0], f"\nImages have different sizes!\n{result[1]}"
