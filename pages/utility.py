import requests
import os
import re

download_dir = '../downloads'

def check_img(images):
	ident = 1
	list_of_sizes = []
	w, h = -1, -1
	str_out = ''
	index = 0
	for img in images:
		width = img.get_attribute("width")
		height = img.get_attribute("height")
		list_of_sizes.append(f'img_{index + 1}: w={width}, h={height}  ')
		if index != 0 and (width != w or height != h):
			ident *= 0
		w, h = width, height
		index += 1
		str_out = ''.join(list_of_sizes)
	if ident:
		print(f'\nImages are identical\n. {str_out}')
	else:
		print(f"\nImages NOT identical! {str_out}")
	return ident

def download(file_link, size):

	filename = os.path.basename(file_link)
	full_path = os.path.join(download_dir, filename)
	with requests.get(file_link, stream=True) as r:
		print(f"\nStart downloading file with size {size}: ", end='')
		r.raise_for_status()
		with open(full_path, 'wb') as f:
			for chunk in r.iter_content(chunk_size=32000):
				if chunk:
					print('.', end='')
					f.write(chunk)
	if os.path.exists(full_path) and os.path.getsize(full_path) >= size:
		print(f"\nFile '{filename}' downloaded {download_dir}")
		print(f"Size of file: {os.path.getsize(full_path) / (1024 * 1024)}")
		return True
	else:
		print(f"Error downloading {filename}")

def get_size(s):
	pattern = r'\d+\.\d+'
	number = float(re.search(pattern, s).group())
	return number

