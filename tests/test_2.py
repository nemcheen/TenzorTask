from pages.base_page import BasePage
from pages.partners_page import PartnersPage
from pages.locators import Locators
import time

url1 = 'https://sbis.ru/'
url2 = 'https://saby.ru/contacts'

def test_region(driver):
    page = BasePage(driver)
    page.driver.get(url1)
    page.check_click(Locators.contacts_loc)
    region_block = page.check_exists_and_find(Locators.region).text
    childs = page.check_child(Locators.partners_block, Locators.one_partner)
    assert region_block and len(childs) > 1, "\nRegion or partners is empty!!"
    print(f"\nRegion is {region_block} as expected and Qty of partners is {len(childs)}\n")

def test_change_region(driver):
    page = PartnersPage(driver)
    page.driver.get(url2)
    default_region = page.get_partner_name()
    default_partners = page.get_partners_list()
    print(default_region)
    print(default_partners)
    page.change_partner(Locators.target_partner)
    time.sleep(5)
    changed_region = page.get_partner_name()
    changed_partners = page.get_partners_list()
    condition_1 = default_region != changed_region and default_partners != changed_partners
    if condition_1:
        print(f"\nRegion changed from '{default_region}' to '{changed_region}'\n")
    print(changed_region)
    print(changed_partners)
    print(page.driver.title)
    print(page.driver.current_url)
    condition_2 =  Locators.target_region_str in page.driver.title
    if condition_2:
        print(f"\nPage title changed to '{page.driver.title}'\n")
    condition_3 = Locators.target_region_EN_str in page.driver.current_url
    if condition_3:
        print(f"\nPage url is '{page.driver.current_url}'\n")

    assert condition_3 and condition_2 and condition_1, \
        f"\nSome conditions failed!\n"









