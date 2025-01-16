from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import Locators
from pages.locators import dynamic_locator
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

MAXTIME = 10

class PartnersPage(BasePage):

	def __init__(self, driver):
		super().__init__(driver)

	def get_region_name(self):
		element = self.wait_and_find(Locators.region)
		text = element.text
		return text

	def change_partner(self, target_partner_locator):
		actions = ActionChains(self.driver)
		element = self.wait_and_find(Locators.region)
		actions.move_to_element(element).click().perform()
		self.wait_click(target_partner_locator)
		self.wait_and_find(dynamic_locator(Locators.target_region_str))
		# self.wait_staleness(dynamic_locator(previous_region))

	def wait_staleness(self, locator):
		element = self.driver.find_element(*locator)
		print(locator)
		WebDriverWait(self.driver, 10).until(EC.staleness_of(element))

	def get_partners_list(self):
		childs = self.check_child(Locators.region, Locators.one_partner)
		partners_list = []
		for child in childs:
			partners_list.append(child.get_attribute("title"))
		return ' ,'.join(partners_list)



