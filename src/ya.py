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
pyautogui.moveTo(1000, 115, duration=0.5)
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
# 以下mac
pyautogui.hotkey('command', 'v')
# 以下win
# pyautogui.hotkey('ctr', 'v')
time.sleep(0.5)

# カテゴリ選択へ
pyautogui.moveTo(50, 650, duration=1.0)
time.sleep(0.5)
pyautogui.click()
time.sleep(0.5)

# カテゴリ検索へ
pyautogui.moveTo(140, 630, duration=1.0)
# クリックして商品名記入
time.sleep(0.5)
pyautogui.click()
time.sleep(0.5)
pyautogui.click()
time.sleep(0.5)
search_ward = "抵抗器単体"
pyperclip.copy(search_ward)
time.sleep(0.5)

#以下のコマンドmacとwinで分ける必要がある。
# 以下mac
time.sleep(0.5)
pyautogui.hotkey('command', 'a')
time.sleep(0.5)
pyautogui.hotkey('command', 'v')
# 以下win
# pyautogui.hotkey('ctr', 'v')
time.sleep(0.5)

# 検索ボタンへ移動クリック
pyautogui.moveTo(800, 630, duration=1.0)
time.sleep(0.5)
pyautogui.click()
time.sleep(0.5)

# スクロール
pyautogui.vscroll(-8)
time.sleep(0.5)

# カテゴリを選択
pyautogui.moveTo(40, 580, duration=1.0)
time.sleep(0.5)
pyautogui.click()
time.sleep(0.5)
pyautogui.vscroll(-10)
time.sleep(0.5)
pyautogui.moveTo(500, 620, duration=1.0)
time.sleep(0.5)
pyautogui.click()
time.sleep(0.5)


# 状態選択
pyautogui.moveTo(140, 350, duration=1.0)
time.sleep(0.5)
pyautogui.click()
time.sleep(0.5)
pyautogui.vscroll(-10)
time.sleep(0.5)
pyautogui.moveTo(140, 780, duration=1.0)
time.sleep(0.5)
pyautogui.click()
time.sleep(0.5)
pyautogui.moveTo(140, 650, duration=1.0)
time.sleep(0.5)
pyautogui.click()


# 横いってクリック
time.sleep(0.5)
pyautogui.moveTo(650, 650, duration=1.0)
time.sleep(0.5)
pyautogui.click()

# スクロール
time.sleep(0.5)
pyautogui.vscroll(-10)

# テキスト入力
time.sleep(0.5)
pyautogui.click()
time.sleep(0.5)
pyautogui.click()
test_ward = "この商品はとてもいいです。"
pyperclip.copy(test_ward)
time.sleep(0.5)
pyautogui.hotkey('command', 'a')
time.sleep(0.5)
pyautogui.hotkey('command', 'v')

# 上移動しクリックスクロール
time.sleep(0.5)
pyautogui.moveTo(650, 250, duration=1.0)
time.sleep(0.5)
pyautogui.click()
pyautogui.vscroll(-10)


# 発送地域選択
time.sleep(0.5)
pyautogui.moveTo(140, 650, duration=1.0)
time.sleep(0.5)
pyautogui.click()
time.sleep(0.1)
pyautogui.vscroll(50)
time.sleep(0.3)
pyautogui.vscroll(-50)
time.sleep(0.3)
pyautogui.moveTo(140, 30, duration=1.0)
time.sleep(0.5)
pyautogui.click()
time.sleep(0.5)
pyautogui.moveTo(650, 650, duration=1.0)
time.sleep(0.5)
pyautogui.click()
time.sleep(0.5)


#送料負担選択
pyautogui.moveTo(140, 800, duration=1.0)
time.sleep(0.5)
pyautogui.click()
time.sleep(0.5)
pyautogui.moveTo(140, 760, duration=1.0)
time.sleep(0.5)
pyautogui.click()
time.sleep(0.5)
pyautogui.moveTo(650, 650, duration=1.0)
time.sleep(0.5)
pyautogui.click()


# 発送方法選択
time.sleep(0.5)
pyautogui.vscroll(-26)
time.sleep(0.5)
pyautogui.moveTo(40, 660, duration=1.0)
time.sleep(0.5)
pyautogui.click()
time.sleep(0.5)
pyautogui.click()

#配送会社指定
time.sleep(0.5)
pyautogui.moveTo(100, 660, duration=1.0)
time.sleep(0.5)
pyautogui.click()
time.sleep(0.5)
pyautogui.vscroll(-20)
pyautogui.moveTo(100, 710, duration=1.0)
time.sleep(0.5)
pyautogui.click()
time.sleep(0.5)
pyautogui.moveTo(140, 710, duration=1.0)
time.sleep(0.5)
pyautogui.click()
price = "780"
pyperclip.copy(price)
time.sleep(0.5)
pyautogui.hotkey('command', 'a')
time.sleep(0.5)
pyautogui.hotkey('command', 'v')


# 発送までの期間を決める
time.sleep(0.5)
pyautogui.vscroll(-10)
time.sleep(0.5)
pyautogui.moveTo(140, 500, duration=1.0)
time.sleep(0.5)
pyautogui.click()
time.sleep(0.5)
pyautogui.moveTo(140, 490, duration=1.0)
time.sleep(0.5)
pyautogui.click()
time.sleep(0.5)
pyautogui.moveTo(400, 490, duration=1.0)
time.sleep(0.5)


# 値段入力
pyautogui.vscroll(-10)
time.sleep(0.5)
pyautogui.moveTo(40, 450, duration=1.0)
time.sleep(0.5)
pyautogui.click()
price = "5000"
pyperclip.copy(price)
time.sleep(0.5)
pyautogui.hotkey('command', 'a')
time.sleep(0.5)
pyautogui.hotkey('command', 'v')
# 即決価格設定
time.sleep(0.5)
pyautogui.moveTo(40, 490, duration=1.0)
time.sleep(0.5)
pyautogui.click()
time.sleep(0.5)
pyautogui.moveTo(40, 530, duration=1.0)
time.sleep(0.5)
pyautogui.click()
decision_price = str(int(price) + 200) 
pyperclip.copy(decision_price)
time.sleep(0.5)
pyautogui.hotkey('command', 'a')
time.sleep(0.5)
pyautogui.hotkey('command', 'v')


# 終了する日時
time.sleep(0.5)
pyautogui.moveTo(40, 700, duration=1.0)
time.sleep(0.5)
pyautogui.click()
time.sleep(0.5)
pyautogui.moveTo(40, 630, duration=1.0)
time.sleep(0.5)
pyautogui.click()
time.sleep(0.5)
pyautogui.moveTo(40, 760, duration=1.0)
time.sleep(0.5)
pyautogui.click()
time.sleep(0.5)
pyautogui.moveTo(40, 810, duration=1.0)
time.sleep(0.5)
pyautogui.click()
time.sleep(0.5)
pyautogui.moveTo(40, 770, duration=1.0)
time.sleep(0.5)
pyautogui.click()
time.sleep(0.5)
pyautogui.moveTo(400, 770, duration=1.0)
time.sleep(0.5)
pyautogui.click()
pyautogui.vscroll(-26)
# 金額入力
# time.sleep(0.5)
# pyautogui.moveTo(140, 710, duration=1.0)
# time.sleep(0.5)
# pyautogui.click()
# price = "780"
# pyperclip.copy(price)
# time.sleep(0.5)
# pyautogui.hotkey('command', 'a')
# time.sleep(0.5)
# pyautogui.hotkey('command', 'v')


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