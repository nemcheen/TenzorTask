from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import Locators as loc, region_to_choose
from pages.locators import header_region
from selenium.webdriver.common.action_chains import ActionChains

MAXTIME = 15

class PartnersPage(BasePage):

	def __init__(self, driver):
		super().__init__(driver)

	def click_hover(self, locator):
		actions = ActionChains(self.driver)
		element = self.wait_clickable_and_find(locator)
		actions.move_to_element(element).click().perform()


	def change_partner(self, name_of_new_region):
		self.click_hover(loc.region_locator)
		self.wait_click(region_to_choose(name_of_new_region))
		self.wait(header_region(name_of_new_region))

	def get_region_name(self):
		element = self.wait_and_find(loc.region_locator)
		text = element.text
		return text

	def get_partners_list(self):
		childs = self.driver.find_elements(*loc.partner_name)
		partners_list = []
		for child in childs:
			partners_list.append(child.get_attribute("title"))
		return ' ,'.join(partners_list)

	def get_name_and_list(self):
		return self.get_region_name(), self.get_partners_list()



