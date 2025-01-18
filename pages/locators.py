from selenium.webdriver.common.by import By

def header_region(name_of_region):
	compiled_locator = (By.XPATH, f"//*[contains(@class, 'sbis_ru-Region-Chooser__text') and contains(text(), '{name_of_region}')]")
	return compiled_locator

def region_to_choose(name_of_region):
	compiled_locator = (By.XPATH, f'//*[@id="popup"]//descendant::span[contains(text(), "{name_of_region}")]')
	return compiled_locator

class Locators:
	parent_loc = (By.XPATH, './parent::*')
	contacts_loc = (By.XPATH, '//a[contains(text(), "Контакты")]')

	work_block = (By.XPATH, '//h2[text()="Работаем"]')
	image = (By.CSS_SELECTOR, 'img.tensor_ru-About__block3-image')

	tenzor_banner = (By.XPATH, '//*[@id="contacts_clients"]/descendant::a[@href="https://tensor.ru/"]/img')
	power_in_human_block = (By.XPATH, '//p[contains(text(), "Сила в людях")]')
	about_link = (By.XPATH, '//a[@href="/about" and text()="Подробнее"]')

	region_locator = (By.CSS_SELECTOR, ".sbis_ru-Region-Chooser__text")

	partner_name = (By.CSS_SELECTOR, '.sbisru-Contacts-List__name')

	download_block = (By.LINK_TEXT, "Скачать локальные версии")
	download_container = (By.XPATH, "//h3[contains(text(), 'Веб-установщик')]")
	link_to_find = (By.CSS_SELECTOR, 'a[href$=".exe"]')

