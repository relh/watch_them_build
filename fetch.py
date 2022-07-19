#!/usr/bin/env python
# -*- coding: utf-8 -*-


import datetime
import pdb
import time
from io import BytesIO

import requests
from PIL import Image
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

url1 = 'https://cam-leinweber1.fo.umich.edu/axis-cgi/jpg/image.cgi'
url2 = 'https://cam-leinweber2.fo.umich.edu/axis-cgi/jpg/image.cgi'

'''
response1 = requests.get(url1)
response2 = requests.get(url2)

img1 = Image.open(BytesIO(response1.content))
img2 = Image.open(BytesIO(response2.content))

pdb.set_trace()
'''

def save_im_from_url(fox, url, cam):
    fox.get(url)

    element = fox.find_element_by_xpath("//img")#.get_attribute("src")

    location = element.location
    size = element.size
    png = fox.get_screenshot_as_png() # saves screenshot of entire page
    #fox.quit()

    im = Image.open(BytesIO(png)) # uses PIL library to open image in memory

    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']

    im = im.crop((left, top, right, bottom)) # defines crop points
    stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    im.save(f'./data/{cam}/{cam}-{stamp}.png') # saves new cropped image
    print(f'./data/{cam}/{cam}-{stamp}.png')


fox = webdriver.Firefox()
count_so_far = 0
while True:
    count_so_far += 1
    stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    print(f'{count_so_far}... {stamp}')

    cdate = datetime.datetime.strftime(datetime.datetime.now(), "%d-%m-%Y")
    if (datetime.datetime.strptime(cdate + " 05:30:00", "%d-%m-%Y %H:%M:%S") <= datetime.datetime.now() <= datetime.datetime.strptime(cdate + " 21:30:00", "%d-%m-%Y %H:%M:%S")):
        save_im_from_url(fox, url1, 'cam1')
        save_im_from_url(fox, url2, 'cam2')
    time.sleep(30)
