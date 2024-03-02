from selenium import webdriver

# Chrome driver file path
chrome_driver_path = "/Applications/chromedriver"

# Create webdriver object
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# get google.co.in
driver.get("https://www.amazon.in")

# driver.close() # This script will close the last opened tab.
driver.quit() # This script will quit the whole browser.