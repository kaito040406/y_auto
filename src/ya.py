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
import pyperclip


# ブラウザ操作
# mail_adress = "ynck630vwte@yahoo.co.jp"
# pass_ward = "dmvb@15773"
# options = Options()
# driver = webdriver.Chrome(chrome_options=options)

# 出品画面にアクセス
# url = "https://auctions.yahoo.co.jp/sell/jp/show/submit?category=0"
# driver.get(url)
# driver.delete_all_cookies()
# time.sleep(5)
# element = driver.find_element_by_id("username");
# element.send_keys(mail_adress)
# time.sleep(3)
# driver.find_element_by_id('btnNext').click();
# time.sleep(3)
# element = driver.find_element_by_id("passwd");
# element.send_keys(pass_ward)
# time.sleep(3)
# driver.find_element_by_id('btnSubmit').click();
# time.sleep(4)
# driver.find_element_by_id('back_originalpage').click();

# -------------------
# 自分でログインする
# ynck630vwte@yahoo.co.jp
# dmvb@15773
# -------------------


# -------------------
# 画像データを引っ張ってくる

# target_dir = 'images/active'
# time.sleep(1)
# shutil.rmtree(target_dir)
# os.mkdir(target_dir)
# time.sleep(1)
# new_path = shutil.move('images/stock/image' + "1", 'images/active/')
# time.sleep(1)
# pyautogui.click(x=300, y=300)
# time.sleep(1)
# -------------------


# 初期ポジ
pyautogui.moveTo(1, 1, duration=0)
time.sleep(0.5)
# データの場所に行く
pyautogui.moveTo(1020, 115, duration=0.5)
time.sleep(0.5)
# ここで本当はドラッグコマンド
pyautogui.moveTo(500, 700, duration=1.0)
# いったんスクロール
time.sleep(0.5)
pyautogui.vscroll(-10)
# 商品名へ移動
time.sleep(0.5)
pyautogui.moveTo(50, 500, duration=1.0)
# クリックして商品名記入
time.sleep(0.5)
pyautogui.click()
time.sleep(0.5)
pyautogui.click()
# テキスト記入
time.sleep(0.5)
text = "テスト"
pyperclip.copy(text)
time.sleep(0.5)
#以下のコマンドmacとwinで分ける必要がある。
pyautogui.hotkey('command', 'v')
# screen_x,screen_y = pyautogui.size()
# pyautogui.moveRel(1370, 40, 0)
# time.sleep(0.5)
# pyautogui.dragTo(400, 400, 0.5, button='left')





# driver.quit()

# element = driver.find_element_by_id("twotabsearchtextbox")
# element.submit()
# search_url = driver.current_url
# time.sleep(0.5)
# driver.quit()
# time.sleep(0.5)
# ブラウザ操作