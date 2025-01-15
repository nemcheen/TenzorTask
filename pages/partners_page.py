from pages.base_page import BasePage
from pages.locators import Locators
from selenium.webdriver.common.action_chains import ActionChains

MAXTIME = 10

class PartnersPage(BasePage):

	def __init__(self, driver):
		super().__init__(driver)

	def get_partner_name(self):
		return self.check_exists_and_find(Locators.region).text

	def change_partner(self, target_partner_locator):
		actions = ActionChains(self.driver)
		element = self.check_exists_and_find(Locators.region)
		actions.move_to_element(element).click().perform()
		return self.check_click(target_partner_locator)

	def get_partners_list(self):
		childs = self.check_child(Locators.region, Locators.one_partner)
		partners_list = []
		for child in childs:
			partners_list.append(child.get_attribute("title"))
		return ' ,'.join(partners_list)


