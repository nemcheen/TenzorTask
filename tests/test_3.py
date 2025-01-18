from pages.base_page import BasePage
from pages.locators import Locators as loc
from pages.utility import download_and_check, get_size_from_page

url = 'https://sbis.ru/'

def test_download(driver):
	page = BasePage(driver)
	page.driver.get(url)
	page.wait_click(loc.download_block)
	link_element = page.find_any_nested(loc.download_container, loc.link_to_find)[0]
	file_link = link_element.get_attribute('href')
	raw_size = link_element.text
	size = get_size_from_page(raw_size)
	assert download_and_check(file_link, size), "File downloading fail!"
