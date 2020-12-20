from selenium import webdriver
import time
from urllib.request import urlopen
import os

search = '마스크 착용한 사람'
url = "https://search.naver.com/search.naver?where=image&section=image&query=" + search

browser = webdriver.Chrome('C:\chromedriver')
browser.implicitly_wait(3)
browser.get(url)
time.sleep(1)

for _ in range(10000):
    browser.execute_script("window.scrollBy(0,30000)")

count = 0
image_list = []

image_list = browser.find_elements_by_tag_name("span.img_border")

if not os.path.exists(search):
    os.mkdir(search)

for index, img in enumerate(image_list[0:]):
    img.click()
    html_objects = browser.find_element_by_tag_name('img._image_source')
    current_src = html_objects.get_attribute('src')

    t = urlopen(current_src).read()
    if index < 1000:
        filename = search + str(count) + ".png"
        File = open(os.path.join(search, "image_" + str(count) + ".png"), "wb")
        File.write(t)
        count += 1
    else:
        browser.close()
        break

