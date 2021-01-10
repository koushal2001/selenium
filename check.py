
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome("/home/koushal/selenium/chromedriver")   # Selenium chromedriver path

driver.get("https://web.whatsapp.com/")

name=input("Enter the Target Name after scanning QR code.\n ")
user = driver.find_element_by_xpath("//span[@title='{}']".format(name))
user.click()

text_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
for i in range(500):
    text_box.send_keys("Good Morning"+Keys.ENTER)
driver.quit()

