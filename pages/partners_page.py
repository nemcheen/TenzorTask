from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import Locators as LOC, region_to_choose
from pages.locators import header_region
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

MAXTIME = 10

class PartnersPage(BasePage):

	def __init__(self, driver):
		super().__init__(driver)



	def change_partner(self, name_of_new_region):

		actions = ActionChains(self.driver)
		element = self.wait_and_find(LOC.region_locator)
		actions.move_to_element(element).click().perform()
		self.wait_click(LOC.target_region) # !
		self.wait_and_find(header_region(name_of_new_region))

		# self.wait_and_find(dynamic_locator(LOC.target_region_str))

		# actions = ActionChains(self.driver)
		# element = self.wait_and_find(Locators.region)
		# actions.move_to_element(element).click().perform()
		# self.wait_click(target_partner_locator)
		# self.wait_and_find(dynamic_locator(Locators.target_region_str))
		# self.wait_staleness(dynamic_locator(previous_region))

	def wait_staleness(self, locator):
		element = self.driver.find_element(*locator)
		print(locator)
		WebDriverWait(self.driver, 10).until(EC.staleness_of(element))

	def get_region_name(self):
		element = self.wait_and_find(LOC.region_locator)
		text = element.text
		return text

	def get_partners_list(self):
		childs = self.driver.find_elements(*LOC.partner_name)
		partners_list = []
		for child in childs:
			partners_list.append(child.get_attribute("title"))
		return ' ,'.join(partners_list)

	def get_name_and_list(self):
		return self.get_region_name(), self.get_partners_list()



