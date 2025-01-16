from pages.base_page import BasePage
from pages.partners_page import PartnersPage
from pages.locators import Locators
import time

url1 = 'https://sbis.ru/'
# url2 = 'https://saby.ru/contacts'
target_region_str = 'Камчатский'
target_url_str = 'kamchatskij'

'<span class="sbis_ru-Region-Chooser__text sbis_ru-link">Свердловская обл.</span>'
"//h1[text()='Контакты']//parent::div//parent::div//descendant::span[text()='Свердловская обл.' and contains(@class,'Region-Chooser')]"
'//span[text()="Свердловская обл." and contains(@class,"Region-Chooser")]'
"//h1[text()='Контакты']//parent::*//parent::*//descendant::*[text()='Свердловская обл.']"

def test_region(driver):
    page = PartnersPage(driver)
    page.driver.get(url1)
    page.wait_click(Locators.contacts_loc)
    region_block = page.wait_and_find(Locators.region).text
    childs = page.check_child(Locators.partners_block, Locators.one_partner)
    assert region_block and len(childs) > 1, (f"\nRegion or partners is empty!!,"
                                              f"\nRegion is {region_block}. Qty of partners is {len(childs)}\n")
    default_region = page.get_region_name()
    default_partners = page.get_partners_list()
    page.change_partner(Locators.target_region)
    changed_region = page.get_region_name()
    changed_partners = page.get_partners_list()
    condition_1 = default_region != changed_region and default_partners != changed_partners
    assert condition_1, f"\nError changing region and getting list pf partners.\nprevious region is '{default_region}'\nnew region is '{changed_region}'"
    condition_2 =  target_region_str in page.driver.title
    assert condition_2, f"\nError region title. Page title changed to '{page.driver.title}'"
    condition_3 = target_url_str in page.driver.current_url
    assert condition_3, f"\nPage url error. Url after test is'{page.driver.current_url}'"









