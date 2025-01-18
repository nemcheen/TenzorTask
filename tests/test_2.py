from pages.partners_page import PartnersPage
from pages.locators import Locators as loc

URL = 'https://sbis.ru/'
TARGET_REGION_STR = 'Камчатский'
TARGET_REGION_URL = 'kamchatskij'

def test_region(driver):
    page = PartnersPage(driver)
    page.driver.get(URL)
    page.wait_click(loc.contacts_loc)
    partner_name_str = page.wait_and_find(loc.region_locator).text
    list_of_partners = page.driver.find_elements(*loc.partner_name)
    assert partner_name_str and len(list_of_partners) > 1, (f"\nRegion or partners is empty!!,"
                                              f"\nRegion is {partner_name_str}. Qty of partners is {len(list_of_partners)}\n")
    default_region, default_partners = page.get_name_and_list()
    page.change_partner(TARGET_REGION_STR)
    changed_region, changed_partners = page.get_name_and_list()
    assert default_region != changed_region, f"\nError changing region \nregion is '{changed_region}'"
    assert default_partners != changed_partners, f"\nPartners list not changed \n'{changed_partners}'"
    assert TARGET_REGION_STR in page.driver.title, f"\nPage title changed to '{page.driver.title}'"
    assert TARGET_REGION_URL in page.driver.current_url, f"\nUrl after test is'{page.driver.current_url}'"





