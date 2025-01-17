from pages.base_page import BasePage
from pages.locators import Locators as loc
from pages.utility import download_and_check, get_size_from_page

url = 'https://sbis.ru/'

def test_download(driver):
	page = BasePage(driver)
	page.driver.get(url)
	page.wait_click(loc.download_block)

	first_elem = page.wait_and_find(loc.download_container)
	second_elem = first_elem.find_element(*loc.link)
	file_link = second_elem.get_attribute('href')
	raw_size = second_elem.text
	size = get_size_from_page(raw_size)
	assert download_and_check(file_link, size), "File downloading fail!"
