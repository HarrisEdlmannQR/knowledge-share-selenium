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

# Click SSO button
sso_button = driver.find_element(by=By.ID, value="sso")
sso_button.click()

# Input email and click 'Next'
email = "harris.edlmann@quickrelease.co.uk"

email_input = driver.find_element(by=By.ID, value="i0116")
email_input.send_keys(email)

email_next_button = driver.find_element(by=By.ID, value="idSIButton9")
email_next_button.click()

time.sleep(10) # discuss implicitly_wait

# Input password and click 'Sign in'
password = pwinput.pwinput(prompt="Enter Password: ", mask="*")
print(f"Password Received!")

password_input = driver.find_element(by=By.ID, value="i0118")
password_input.send_keys(password)

password_sign_in_button = driver.find_element(by=By.ID, value="idSIButton9")
password_sign_in_button.click()

# Input Authentication code and click 'Verify'
auth_code = pwinput.pwinput(prompt="Enter Authentication code: ", mask="*")
print(f"Authenticator Code Received!")

authentication_input = driver.find_element(by=By.ID, value="idTxtBx_SAOTCC_OTC")
authentication_input.send_keys(auth_code)

authentication_verify_button = driver.find_element(by=By.ID, value="idSubmit_SAOTCC_Continue")
authentication_verify_button.click()

time.sleep(2)

# CLick 'Yes' to stay signed in
stay_sign_in_button = driver.find_element(by=By.ID, value="idSIButton9")
stay_sign_in_button.click()

# Get greeting message from homepage
greeting_message = driver.find_element(by=By.XPATH, value="//div[@class='col-lg-8']//div//div//div//div//h3")
print(f"Greeting message is, '{greeting_message.text.rsplit(' ', 1)[0]}'")

driver.quit() # even with 'detach'=True this will close the window