from selenium.webdriver.common.by import By

class Locators:
  contacts_loc = (By.XPATH, '//*[@id="container"]/div[2]/div[1]/div[3]/div[4]/ul/li[1]/a')
  tenzor_banner = (By.XPATH, '//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a')
  power_in_human_block = (By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[1]')
  more_link = (By.XPATH, '//div[@id="container"]/div/div/div[5]/div/div/div/div/p[4]/a')
  parent_div_img = (By.XPATH, '//*[@id="container"]/div[1]/div/div[4]')
  img = (By.XPATH, './/img')
  region = (By.XPATH, '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')
  partners_block = (By.XPATH, '//*[@id="contacts_list"]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]')
  one_partner = (By.XPATH, '//*[@id="contacts_list"]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div/div/div/div[1]/div[1]')
  target_partner = (By.XPATH, '//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span')


  download_block = (By.XPATH, '//*[@id="container"]/div[2]/div[1]/div[3]/div[3]/ul/li[9]/a')
  footer_locator = (By.CSS_SELECTOR, '#container > div.sbisru-Footer.sbisru-Footer__scheme--default > div.sbis_ru-container > div.sbisru-Footer__container')
  footer_element = (By.XPATH, "//*[contains(text(), 'Скачать локальные версии')]")
  download_container = (By.XPATH, "//h3[contains(text(), 'Веб-установщик')]")
  link = (By.XPATH, '../..//div[2]/div/a')

  default_region_str = 'Москва'
  target_region_str = 'Камчатский'
  target_region_EN_str = 'kamchatskij'
