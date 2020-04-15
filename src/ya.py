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
import shutil


# ブラウザ操作
mail_adress = "ynck630vwte@yahoo.co.jp"
pass_ward = "dmvb@15773"
options = Options()
driver = webdriver.Chrome(chrome_options=options)

# 出品画面にアクセス
url = "https://auctions.yahoo.co.jp/sell/jp/show/submit?category=0"
driver.get(url)
driver.delete_all_cookies()
time.sleep(5)
element = driver.find_element_by_id("username");
element.send_keys(mail_adress)
time.sleep(3)
driver.find_element_by_id('btnNext').click();
time.sleep(3)
element = driver.find_element_by_id("passwd");
element.send_keys(pass_ward)
time.sleep(3)
driver.find_element_by_id('btnSubmit').click();
time.sleep(4)
driver.find_element_by_id('back_originalpage').click();

# 画像データを引っ張ってくる

target_dir = 'images/active'
time.sleep(1)
shutil.rmtree(target_dir)
os.mkdir(target_dir)
time.sleep(1)
new_path = shutil.move('images/stock/image' + "1", 'images/active/')
time.sleep(1)
pyautogui.click(x=300, y=300)
time.sleep(1)


# データをドロップする
pyautogui.moveTo(1, 1, duration=0)
time.sleep(0.5)
screen_x,screen_y = pyautogui.size()
pyautogui.moveRel(1370, 40, 0)
time.sleep(0.5)
pyautogui.dragTo(400, 400, 0.5, button='left')





# driver.quit()

# element = driver.find_element_by_id("twotabsearchtextbox")
# element.submit()
# search_url = driver.current_url
# time.sleep(0.5)
# driver.quit()
# time.sleep(0.5)
# ブラウザ操作