import os
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import urllib.request
import time
from random import randint

# URL that we will scrape images from
url = "https://www.pinterest.com/cutestpaw/cutest-animals/"

# Path to our chromedriver
PATH = "D:\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# Start the driver using the given url, then save information in page_source
driver.get(url)
time.sleep(1)
page_source = driver.page_source



# Scroll down X times
elem = driver.find_element_by_tag_name("body")
no_of_pagedowns = 10

elem.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
elem.send_keys(Keys.ESCAPE)
while no_of_pagedowns:
    time.sleep(0.2)
    elem.send_keys(Keys.PAGE_DOWN)
    no_of_pagedowns-=1

time.sleep(1)

# initialize soup with the page_source information from out selenium chrome driver, parse with HTML.
soup = BeautifulSoup(page_source, "html.parser")

# get all images found
images = soup.find_all("img")


# Loop though all images and download them
counter = 0
for image in images:
    image_src = image["src"]
    print(image_src)
    urllib.request.urlretrieve(image_src, str(counter) + ".jpg")
    counter += 1

# Close Chrome driver
driver.quit()

# Remove the first two images, they are not needed
os.remove("0.jpg")
os.remove("1.jpg")

# Pick a random .jpg picture
imageValue = randint(2, counter)
convertedValue = str(imageValue)

# Cleanup all other pictures
for i in range(imageValue - 2):
    temp = str(i + 2)
    os.remove(temp + ".jpg")

for i in range(counter - imageValue - 1):
    temp = str(i + imageValue + 1)
    os.remove(temp + ".jpg")

# Open the selected random .jpg
os.startfile(convertedValue + ".jpg")





