
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



driver=webdriver.Chrome("/home/koushal/selenium/chromedriver")   # Selenium chromedriver path
driver.get("https://www.instagram.com/direct/inbox/")
input()
user = driver.find_element_by_css_selector("#react-root > section > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div.oNO81 > div.Igw0E.IwRSH.eGOV_._4EzTm.i0EQd > div > div > div > div > div:nth-child(1)")
user.click()
text_box = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
for i in range(0,50):
    text_box.send_keys("Dummy Script Test"+Keys.ENTER)

