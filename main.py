from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

URL = "https://tinder.com/"

# ------------ Details -------------
UserName = "Insert your username"
Password = "Insert your password"
# ----------------------------------

chrome_driver_path = "C:/Users/buski/Documents/Development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url=URL)
sleep(3)
login = driver.find_element_by_xpath("//*[@id='t812761606']/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span")
login.click()
sleep(2)

with_facebook = driver.find_element_by_xpath("//*[@id='t-915619470']/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]")
with_facebook.click()
sleep(6)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)
sleep(2)

username = driver.find_element_by_xpath("//*[@id='email']")
username.send_keys(UserName)
password = driver.find_element_by_xpath("//*[@id='pass']")
password.send_keys(Password)
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)
sleep(5)
try:
    driver.find_element_by_xpath("//*[@id='t-915619470']/div/div/div/div/div[3]/button[1]/span").click()
    sleep(1)
    driver.find_element_by_xpath("//*[@id='t-915619470']/div/div/div/div/div[3]/button[1]/span").click()
    sleep(1)
    driver.find_element_by_xpath("//*[@id='t812761606']/div/div[2]/div/div/div[1]/button/span").click()
    sleep(5)
except NoSuchElementException:
    sleep(5)
for _ in range(100):
    sleep(1)
    try:
        body = driver.find_element_by_css_selector('body')
        body.send_keys(Keys.RIGHT)
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            sleep(2)
    except NoSuchElementException:
        sleep(2)

driver.quit()
