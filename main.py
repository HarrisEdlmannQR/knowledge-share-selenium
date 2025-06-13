from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import time
import pwinput

# Define browser options
options = Options()
# add options
options.add_argument("--start-maximized")
# add experimental options: advanced browser settings
options.add_experimental_option("detach", True) # keeps window open after script has finished

# Configure and manage driver executable
service = Service(executable_path="./chromedriver.exe")

# Define the browser instance controlled by the driver
driver = webdriver.Chrome(options=options, service=service)
driver.implicitly_wait(2)

driver.get("https://qrthehub.co.uk/")

"""your code here"""

# driver.quit() # even with 'detach'=True this will close the window