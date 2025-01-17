import requests
import os
import re

download_dir = '../downloads'

def check_images(images):
	ident = True
	list_of_sizes = []
	w, h = None, None
	for index, img in enumerate(images):
		width = img.get_attribute("width")
		height = img.get_attribute("height")
		list_of_sizes.append(f'img_{index + 1}: w={width}, h={height} / ')
		if index == 0:
			w, h = width, height
			continue
		elif width != w or height != h:
			ident = False
	str_out = ''.join(list_of_sizes)
	return ident, str_out

def download_and_check(file_link, size):
	filename = os.path.basename(file_link)
	full_path = os.path.join(download_dir, filename)
	with requests.get(file_link, stream=True) as r:
		r.raise_for_status()
		with open(full_path, 'wb') as f:
			for chunk in r.iter_content(chunk_size=32000):
				if chunk:
					f.write(chunk)
	downloaded_size = round(os.path.getsize(full_path), 2)
	return os.path.exists(full_path) and downloaded_size == size

def get_size_from_page(s):
	pattern = r'\d+\.\d+'
	number = float(re.search(pattern, s).group())
	return number

