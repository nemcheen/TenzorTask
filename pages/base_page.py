from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import Locators as loc

MAXTIME = 15

class BasePage:

	def __init__(self, driver):
		self.driver = driver

	def wait(self, locator):
		WebDriverWait(self.driver, MAXTIME).until(EC.presence_of_element_located(locator))
		return self.driver

	def wait_clickable_and_find(self, locator):
		try:
			WebDriverWait(self.driver, MAXTIME).until(EC.element_to_be_clickable(locator))  # !!!!
			result = self.driver.find_element(*locator)
		except NoSuchElementException:
			return False
		return result

	def wait_and_find(self, locator):
		try:
			self.wait(locator)  # !!!!
			result = self.driver.find_element(*locator)
		except NoSuchElementException:
			return False
		return result
	
	def wait_and_find_all(self, locator):
		try:
			self.wait(locator)
			result = self.driver.find_elements(*locator)
		except NoSuchElementException:
			return False
		return result

	def wait_click(self, locator):
		self.wait_and_find(locator).click()

	def check_url(self, url):
		return WebDriverWait(self.driver, MAXTIME).until(EC.url_to_be(url))

	def check_child(self, parent_locator, child_locator):
		childs = self.wait_and_find(parent_locator).find_elements(*child_locator)
		return childs

	def find_any_nested(self, neighbor_block, any_target_loc):
		current_block = self.driver.find_element(*neighbor_block)
		is_any_element_list = []
		while len(is_any_element_list) == 0:
			is_any_element_list = current_block.find_elements(*any_target_loc)
			current_block = current_block.find_element(*loc.parent_loc)
			if current_block.tag_name == 'html':
				break
		return is_any_element_list


