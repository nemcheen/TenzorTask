from pages.locators import Locators as loc
from pages.download_page import DownloadPage

URL = 'https://sbis.ru/'

def test_download(driver):
	page = DownloadPage(driver)
	page.driver.get(URL)
	page.wait_click(loc.download_block)
	link_element = page.find_any_nested(loc.download_container, loc.link_to_find)[0]
	file_link = link_element.get_attribute('href')
	raw_size = link_element.text
	size = page.get_size_from_page(raw_size)
	assert page.download_and_check(file_link, size), "File downloading fail!"
