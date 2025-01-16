from pages.base_page import BasePage
from pages.locators import Locators
from pages.utility import download, get_size

url = 'https://sbis.ru/'

def test_download(driver):
	page = BasePage(driver)
	page.driver.get(url)
	page.wait_click(Locators.download_block)

	first_elem = page.wait_and_find(Locators.download_container)
	second_elem = first_elem.find_element(*Locators.link)
	file_link = second_elem.get_attribute('href')
	raw_size = second_elem.text
	size = get_size(raw_size)
	assert download(file_link, size), "File downloading fail!"
