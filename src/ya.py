# ブラウザ操作
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary

##PyAutoGUIのモジュール
import pyautogui

##プロセスを制御するためにOS周りのモジュール
import re
import os
import subprocess
import sys
import time
import array


# ブラウザ操作
mail_adress = "akitan_neru@yahoo.co.jp"
pass_ward = "Hamagonn5"
options = Options()
driver = webdriver.Chrome(chrome_options=options)
url = "https://auctions.yahoo.co.jp/sell/jp/show/submit?category=0"
driver.get(url)
time.sleep(5)
# driver.find_element_by_class_name('t_jb9bKlgIcajcRS2hZAP').click();
element = driver.find_element_by_id("username");
element.send_keys(mail_adress)
time.sleep(3)
driver.find_element_by_id('btnNext').click();
time.sleep(3)
element = driver.find_element_by_id("passwd");
element.send_keys(pass_ward)
time.sleep(3)
driver.find_element_by_id('btnSubmit').click();
time.sleep(10)

driver.quit()

# element = driver.find_element_by_id("twotabsearchtextbox")
# element.submit()
# search_url = driver.current_url
# time.sleep(0.5)
# driver.quit()
# time.sleep(0.5)
# ブラウザ操作