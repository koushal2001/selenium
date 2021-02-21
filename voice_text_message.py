import speech_recognition as speech
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

listener = speech.Recognizer()

driver=webdriver.Chrome("/home/koushal/selenium/chromedriver")   # Selenium chromedriver path

driver.get("https://web.whatsapp.com/")

# name=input("Say the Target Name after scanning QR code.\n ")

# with speech.Microphone() as source:
#     print("NOw")
#     message=listener.listen(source)
#     message=listener.recognize_google(message)
#     print(message)
input()

name="Target_name"


user = driver.find_element_by_xpath("//span[@title='{}']".format(name))
user.click()

text_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
with speech.Microphone() as source:
    print("NOw2")
    message=listener.listen(source)
    message=listener.recognize_google(message)
    print(message)
for i in range(10):
    text_box.send_keys(message+Keys.ENTER)
driver.quit()
