import requests
import os
import re
from pages.base_page import BasePage

class DownloadPage(BasePage):

	def __init__(self, driver):
		super().__init__(driver)

	def download_and_check(self, file_link, size):

		current_dir = os.path.dirname(os.path.realpath(__file__))
		filename = os.path.basename(file_link)
		full_path = os.path.join(current_dir, filename)
		with requests.get(file_link, stream=True) as r:
			r.raise_for_status()
			with open(full_path, 'wb') as f:
				for chunk in r.iter_content(chunk_size=8600):
					if chunk:
						f.write(chunk)
		downloaded_size = round(os.path.getsize(full_path) / (1024 * 1024 ), 2)
		return os.path.exists(full_path) and downloaded_size == size

	def get_size_from_page(self, s):
		pattern = r'\d+\.\d+'
		number = float(re.search(pattern, s).group())
		return number

