## Knowledge Share: Web Scraping w/ Selenium

---

### Install drivers

- Chromedriver download link - https://googlechromelabs.github.io/chrome-for-testing/#stable
  - For Chrome, find the url corresponding to **chromedriver** and **win64** for the version of chrome that you have installed. 
Paste the url into your browser to download a zip file and extract the _chromedriver.exe_ file into the repo directory. 
- Edge WebDriver download link - https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver?form=MA13LH

---

### Task: 

Login to the hub using selenium and extract the greeting message it gives you.

### Useful commands

#### Find Element

`find_element` allows you to find an HTML element 
by a specific identifier (information on identifiers below)
```python
element = driver.find_element(by=By.ID, value="<id-value>")
```

#### By
`By` allows you to specify the element's indicator you want to find by
```python
find_element(by=By.ID, value="id")
find_element(by=By.NAME, value="name")
find_element(by=By.XPATH, value="xpath")
find_element(by=By.LINK_TEXT, value="link text")
find_element(by=By.PARTIAL_LINK_TEXT, value="partial link text")
find_element(by=By.TAG_NAME, value="tag name")
find_element(by=By.CLASS_NAME, value="class name")
find_element(by=By.CSS_SELECTOR, value="css selector")
```

> [Useful docs on how to use find_element options.](#https://selenium-python.readthedocs.io/locating-elements.html)

#### Element Actions

Once you have identified an element you may interact with it with commands like:
```python
element.click()
element.send_keys("<string>")
element.clear()
element.submit()
```

#### Mouse Actions

You may interact with elements by simulating mouse actions.
```python
from selenium.webdriver.common.action_chains import ActionChains
actions = ActionChains(driver)

actions.move_to_element(element).perform()
actions.click_and_hold(element).perform()
actions.release().perform()
actions.drag_and_drop(source, target).perform()
actions.double_click(element).perform()
actions.context_click(element).perform()
```

#### Keyboard Actions

You may also simulate keyboard actions.

```python
from selenium.webdriver.common.keys import Keys

Keys.ENTER
Keys.TAB
Keys.ESCAPE
Keys.ARROW_DOWN, Keys.ARROW_UP, etc
Keys.CONTROL
Keys.SHIFT
Keys.ALT

# you can also apply keys multiple times by using *
Keys.TAB * N
```

This can be done to specific elements `elements.send_keys(Keys.<KEY>)` 
or page wide by adding to actions `actions.send_keys(Keys.<KEY>).perform()`

#### Getting element properties

You can extract a variety of bits of information from an element.

```python
element.text
element.get_attribute("<attribute_name>")
element.value_of_css_property("<property_name>")
```

#### Waiting

`driver.implicitly_wait(<seconds>)`:
Sets a global implicit wait time for the WebDriver instance.
It tells Selenium to wait up to a specified time
when trying to find any element(s) if they are not immediately available.

`time.sleep(<seconds>)`: Waits the given amount of time.
