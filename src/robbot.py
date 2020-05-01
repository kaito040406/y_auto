
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
import url_check
import logging
import os_check

def robbot(category ,title, text, price, traffic):
  # OSの確認
  ctr = os_check.use_os()
  # 現在のurl取得
  url = url_check.url_check()
  # 初期ポジ
  logging.info('info %s %s', 'ヤフオクへ画像データをインポート', 'Start')
  pyautogui.moveTo(1, 1, duration=0)
  time.sleep(0.3)
  
  # データの場所に行く
  pyautogui.moveTo(985, 115, duration=0)
  time.sleep(0.3)
  pyautogui.dragTo(500, 700, 0.3, button='left')
  logging.info('info %s %s', 'ヤフオクへ画像データをインポート', 'End')
  # いったんスクロール
  logging.info('info %s %s', '商品タイトル記入', 'Start')
  time.sleep(0.3)
  pyautogui.vscroll(-10)
  # 商品名へ移動
  time.sleep(0.3)
  pyautogui.moveTo(50, 500, duration=0)
  # クリックして商品名記入
  time.sleep(0.3)
  pyautogui.click()
  time.sleep(0.3)
  pyautogui.click()
  # テキスト記入
  time.sleep(0.3)
  pyperclip.copy(title)
  time.sleep(0.3)
  pyautogui.hotkey(ctr, 'v')
  time.sleep(0.3)
  logging.info('info %s %s', '商品タイトル記入', 'End')

  # いったん下でポジションをとる
  pyautogui.vscroll(-3000)
  logging.info('info %s %s', '商品テキスト入力', 'End')

  time.sleep(0.2)
  pyautogui.vscroll(25)
  
  logging.info('info %s %s', '値段', 'Start')
  # 値段入力
  time.sleep(0.3)
  pyautogui.moveTo(50, 590, duration=0)
  time.sleep(0.3)
  pyautogui.click()
  pyperclip.copy(price)
  time.sleep(0.3)
  pyautogui.hotkey(ctr, 'a')
  time.sleep(0.3)
  pyautogui.hotkey(ctr, 'v')
  # 即決価格設定
  url = url_check.url_check_t(url)
  time.sleep(0.3)
  pyautogui.moveTo(50, 640, duration=0)
  time.sleep(0.3)
  pyautogui.click()
  time.sleep(0.3)
  pyautogui.moveTo(50, 680, duration=0)
  time.sleep(0.3)
  pyautogui.click()
  decision_price = str(int(price) + 200) 
  pyperclip.copy(decision_price)
  time.sleep(0.3)
  pyautogui.hotkey(ctr, 'a')
  time.sleep(0.3)
  pyautogui.hotkey(ctr, 'v')
  logging.info('info %s %s', '値段', 'End')
  

  logging.info('info %s %s', '日時設定', 'Start')
  # 終了する日時
  time.sleep(0.3)
  pyautogui.vscroll(-10)
  time.sleep(0.3)
  pyautogui.moveTo(50, 450, duration=0)
  # 540
  time.sleep(0.3)
  pyautogui.click()
  time.sleep(0.2)
  pyautogui.moveTo(50, 400, duration=0)
  time.sleep(0.2)
  pyautogui.click()
  time.sleep(0.1)
  pyautogui.moveTo(50, 450, duration=0)
  time.sleep(0.2)
  pyautogui.click()
  time.sleep(0.2)
  pyautogui.moveTo(50, 420, duration=0)
  time.sleep(0.2)
  pyautogui.click()
  time.sleep(0.2)
  logging.info('info %s %s', '日時設定', 'End')
  pyautogui.vscroll(60)

  logging.info('info %s %s', '商品テキスト入力', 'Start')
  pyautogui.moveTo(190, 650, duration=0)
  time.sleep(0.2)
  pyautogui.click()
  time.sleep(0.2)
  pyautogui.click()
  pyperclip.copy(text)
  time.sleep(0.2)
  pyautogui.hotkey(ctr, 'v')

  time.sleep(0.2)
  pyautogui.moveTo(650, 320, duration=0)
  time.sleep(0.1)
  pyautogui.click()
  pyautogui.vscroll(10)
  logging.info('info %s %s', '商品テキスト入力', 'End')
  
  # url確認
  url = url_check.url_check_t(url)

  
  time.sleep(0.1)
  pyautogui.vscroll(-20)
  

  # カテゴリ選択へ
  logging.info('info %s %s', 'カテゴリチェック', 'Start')
  pyautogui.moveTo(50, 650, duration=0)
  time.sleep(0.3)
  pyautogui.click()
  time.sleep(5)
  url = url_check.url_check_f(url)

  # カテゴリ検索へ
  pyautogui.moveTo(140, 630, duration=0)
  # クリックして商品名記入
  time.sleep(0.3)
  pyautogui.click()
  time.sleep(0.3)
  pyautogui.click()
  time.sleep(0.3)
  pyperclip.copy(category)
  time.sleep(0.3)

  #以下のコマンドmacとwinで分ける必要がある。
  # 以下mac
  time.sleep(0.3)
  pyautogui.hotkey(ctr, 'a')
  time.sleep(0.3)
  pyautogui.hotkey(ctr, 'v')
  # 以下win
  # pyautogui.hotkey('ctr', 'v')
  time.sleep(0.3)

  # 検索ボタンへ移動クリック
  pyautogui.moveTo(800, 630, duration=0)
  time.sleep(0.3)
  pyautogui.click()
  time.sleep(0.3)

  # スクロール
  pyautogui.vscroll(-8)
  time.sleep(0.2)

  # カテゴリを選択
  pyautogui.moveTo(70, 630, duration=0)
  time.sleep(0.2)
  pyautogui.click()
  time.sleep(0.3)
  pyautogui.moveTo(30, 585, duration=0)
  time.sleep(0.3)
  pyautogui.click()
  time.sleep(0.3)
  pyautogui.vscroll(-100)
  time.sleep(0.3)
  url = url_check.url_check_t(url)

  pyautogui.moveTo(550, 575, duration=0)
  time.sleep(0.3)
  pyautogui.click()
  time.sleep(0.2)
  url = url_check.url_check_f(url)
  time.sleep(0.2)
  pyautogui.moveTo(550, 575, duration=0)


  time.sleep(0.3)
  pyautogui.click()
  pyautogui.vscroll(-3000)
  time.sleep(0.3)
  pyautogui.moveTo(480, 690, duration=0)
  time.sleep(0.3)
  pyautogui.click()


  time.sleep(5)
  logging.info('info %s %s', '同意画面', 'Start')
  url = url_check.url_check_f(url)
  time.sleep(0.3)
  pyautogui.moveTo(318, 470, duration=0)
  time.sleep(0.2)
  pyautogui.click()
  time.sleep(0.2)
  pyautogui.moveTo(470, 525, duration=0)
  time.sleep(0.2)
  pyautogui.click()
  logging.info('info %s %s', '同意画面', 'End')

  logging.info('info %s %s', '出品完了画面', 'Start')
  time.sleep(7)
  pyautogui.moveTo(40, 360, duration=0)
  time.sleep(0.3)
  pyautogui.click()
  time.sleep(3)
  pyautogui.moveTo(60, 160, duration=0)
  logging.info('info %s %s', '出品完了画面', 'End')

  logging.info('info %s %s', 'メインページバック', 'Start')
  time.sleep(0.3)
  pyautogui.vscroll(3000)
  time.sleep(0.3)
  pyautogui.moveTo(80, 160, duration=0)
  time.sleep(0.3)
  pyautogui.click()

  time.sleep(2)
  url = url_check.url_check_f(url)
  pyautogui.moveTo(570, 170, duration=0)
  time.sleep(5)
  pyautogui.click()
  time.sleep(0.3)
  pyautogui.hscroll(-3000)
  time.sleep(0.3)
  pyautogui.moveTo(740, 220, duration=0)
  time.sleep(0.3)
  pyautogui.click()
  logging.info('info %s %s', 'メインページバック', 'End')

  # 下書き削除
  time.sleep(5)
  logging.info('info %s %s', '下書き削除', 'Start')
  pyautogui.moveTo(60, 500, duration=0)
  time.sleep(0.3)
  pyautogui.click()
  time.sleep(0.3)
  pyautogui.hscroll(-3000)
  time.sleep(0.3)
  pyautogui.moveTo(740, 600, duration=0)
  time.sleep(0.3)
  pyautogui.click()
  time.sleep(0.3)
  pyautogui.moveTo(480, 500, duration=0)
  time.sleep(0.3)
  pyautogui.click()
  time.sleep(0.7)
  pyautogui.hscroll(3000)
  logging.info('info %s %s', '下書き削除', 'End')

