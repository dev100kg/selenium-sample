import chromedriver_binary

from selenium import webdriver

chromedriver_binary.add_chromedriver_to_path()
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get('https://yahoo.co.jp')
driver.quit()
