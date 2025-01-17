from selenium.webdriver.common.by import By


def header_region(name_of_region):
	compiled_locator = (By.XPATH, f"//*[contains(@class, 'sbis_ru-Region-Chooser__text') and contains(text(), '{name_of_region}')]")

	return compiled_locator

def region_to_choose(name_of_region):
	compiled_locator = (By.XPATH, f'//*[@id="popup"]//descendant::*[contains(text(), "{name_of_region}")]')
	return compiled_locator

class Locators:
	contacts_loc = (By.XPATH, '//a[contains(text(), "Контакты")]')

	tenzor_banner = (By.XPATH, '//*[@id="contacts_clients"]/descendant::a[@href="https://tensor.ru/"]/img')
	'//*[@id="contacts_clients"]/descendant::a[@title="tensor.ru"]'
	'//*[@id="contacts_clients"]/descendant::a[@href="https://tensor.ru/"]'

	power_in_human_block = (By.XPATH, '//*[text()="Сила в людях"]')
	'//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[1]'

	more_link = (By.XPATH, '//a[@href="/about" and text()="Подробнее"]')
	'//div[@id="container"]/div/div/div[5]/div/div/div/div/p[4]/a'

	image = (By.XPATH, '//*[text()="Работаем"]/parent::*/parent::*/descendant::img')
	'//*[text()="Работаем"]/parent::*/parent::*/descendant::img'

	region_locator = (By.CSS_SELECTOR, ".sbis_ru-Region-Chooser__text")
	'(By.CSS_SELECTOR, ".sbis_ru-Region-Chooser__text")'
	'//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span'

	partners_block = (By.XPATH, '//*[@id="contacts_list"]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]')



	partner_name = (By.CSS_SELECTOR, '.sbisru-Contacts-List__name')
	'.sbisru-Contacts-List__name'
	'<div title="Saby - Камчатка" class="sbisru-Contacts-List__name sbisru-Contacts-List--ellipsis sbisru-Contacts__text--md pb-4 pb-xm-12 pr-xm-32" itemprop="name">Saby - Камчатка</div>'

	# target_region = (By.XPATH, '//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span')

	download_block = (By.XPATH, '//*[@id="container"]/div[2]/div[1]/div[3]/div[3]/ul/li[9]/a')
	footer_locator = (By.CSS_SELECTOR, '#container > div.sbisru-Footer.sbisru-Footer__scheme--default > div.sbis_ru-container > div.sbisru-Footer__container')
	footer_element = (By.XPATH, "//*[contains(text(), 'Скачать локальные версии')]")
	download_container = (By.XPATH, "//h3[contains(text(), 'Веб-установщик')]")
	link = (By.XPATH, '../..//div[2]/div/a')

	# default_region_str = 'Москва'
	target_region_str = 'Камчатский'
	target_region_EN_str = 'kamchatskij'
