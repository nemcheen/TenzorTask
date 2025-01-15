from pages.base_page import BasePage
from pages.locators import Locators
from pages.utility import check_img

about_url = 'https://tensor.ru/about'
url1 = "https://sbis.ru"
url2 = 'https://tensor.ru/'
url3 = 'https://tensor.ru/about'

def test_find_power(driver):
    contacts_page = BasePage(driver)
    contacts_page.driver.get(url1)
    contacts_page.check_click(Locators.contacts_loc)
    contacts_page.check_click(Locators.tenzor_banner)
    element = contacts_page.check_exists_and_find(Locators.power_in_human_block)
    assert element, "No 'Power in Human' block"
    print("\nBlock 'Power in human' is present")

def test_about_block(driver):
    next_page = BasePage(driver)
    next_page.driver.get(url2)
    next_page.check_click(Locators.more_link)
    assert next_page.check_url(about_url), "Page https://tensor.ru/about not opened"
    print("\nPage https://tensor.ru/about opened")

def test_compare_img(driver):
    next_page = BasePage(driver)
    next_page.driver.get(url3)
    parent_div = next_page.check_exists_and_find(Locators.parent_div_img)
    img_elements = parent_div.find_elements(*Locators.img)
    result = check_img(img_elements)
    assert result, "\nImages have different sizes!"
    # ident = 0
    # list_of_sizes = []
    # w, h = -1, -1
    # str_out = ''
    # index = 0
    # for img in img_elements:
    #     width = img.get_attribute("width")
    #     height = img.get_attribute("height")
    #     list_of_sizes.append(f'img_{index + 1}: w={width}, h={height}  ')
    #     if index != 0 and( width != w or height != h ):
    #         ident+=1
    #     w, h = width, height
    #     index+=1
    #     str_out = ''.join(list_of_sizes)
    # assert ident == 0, f"\nImages NOT identical! {str_out}"
    # print(f'\nImages are identical\n. {str_out}')
