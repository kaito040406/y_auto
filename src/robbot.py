
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

def robbot(category ,title, text, price, traffic):
  # 現在のurl取得
  url = url_check.url_check()
  # 初期ポジ
  logging.info('info %s %s', 'ヤフオクへ画像データをインポート', 'Start')
  pyautogui.moveTo(1, 1, duration=0)
  time.sleep(0.3)
  # データの場所に行く
  pyautogui.moveTo(1000, 115, duration=0)
  time.sleep(0.5)
  pyautogui.dragTo(500, 700, 0.5, button='left')
  logging.info('info %s %s', 'ヤフオクへ画像データをインポート', 'End')
  # いったんスクロール
  logging.info('info %s %s', '商品タイトル記入', 'Start')
  time.sleep(0.5)
  pyautogui.vscroll(-10)
  # 商品名へ移動
  time.sleep(0.5)
  pyautogui.moveTo(50, 500, duration=0.5)
  # クリックして商品名記入
  time.sleep(0.5)
  pyautogui.click()
  time.sleep(0.5)
  pyautogui.click()
  # テキスト記入
  time.sleep(0.5)
  pyperclip.copy(title)
  time.sleep(0.5)
  pyautogui.hotkey('command', 'v')
  time.sleep(0.5)
  logging.info('info %s %s', '商品タイトル記入', 'End')

  # url確認
  url = url_check.url_check_t(url)

  # カテゴリ選択へ
  logging.info('info %s %s', 'カテゴリチェック', 'Start')
  pyautogui.moveTo(50, 650, duration=0.5)
  time.sleep(0.5)
  pyautogui.click()
  time.sleep(5)
  url = url_check.url_check_f(url)

  # カテゴリ検索へ
  pyautogui.moveTo(140, 630, duration=0.5)
  # クリックして商品名記入
  time.sleep(0.5)
  pyautogui.click()
  time.sleep(0.5)
  pyautogui.click()
  time.sleep(0.5)
  pyperclip.copy(category)
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
  pyautogui.moveTo(800, 630, duration=0.5)
  time.sleep(0.5)
  pyautogui.click()
  time.sleep(0.5)

  # スクロール
  pyautogui.vscroll(-8)
  time.sleep(0.2)

  # カテゴリを選択
  pyautogui.moveTo(750, 630, duration=0.5)
  time.sleep(0.2)
  pyautogui.click()
  time.sleep(0.5)
  pyautogui.moveTo(30, 585, duration=0.5)
  time.sleep(0.5)
  pyautogui.click()
  time.sleep(0.5)
  pyautogui.vscroll(-100)
  time.sleep(0.5)

  url = url_check.url_check_t(url)

  pyautogui.moveTo(550, 575, duration=0.5)
  time.sleep(0.5)
  pyautogui.click()
  time.sleep(0.2)
  url = url_check.url_check_f(url)
  logging.info('info %s %s', 'カテゴリチェック', 'End')
  logging.info('info %s %s', '商品テキスト入力', 'Start')
  time.sleep(0.2)
  pyautogui.moveTo(550, 575, duration=0)
  time.sleep(0.5)
  pyautogui.vscroll(-10)


  # 横いってクリック
  time.sleep(0.5)
  pyautogui.moveTo(650, 750, duration=0)
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
  pyperclip.copy(text)
  time.sleep(0.5)
  pyautogui.hotkey('command', 'a')
  time.sleep(0.5)
  pyautogui.hotkey('command', 'v')
  logging.info('info %s %s', '商品テキスト入力', 'End')

  logging.info('info %s %s', '商品テキスト', 'Start')
  # 上移動しクリックスクロール
  time.sleep(0.5)
  url = url_check.url_check_t(url)
  pyautogui.moveTo(650, 350, duration=0.5)
  time.sleep(0.5)
  pyautogui.click()
  pyautogui.vscroll(-50)

  # 値段入力
  time.sleep(0.5)
  pyautogui.moveTo(50, 670, duration=0.5)
  time.sleep(0.5)
  pyautogui.click()
  pyperclip.copy(price)
  time.sleep(0.5)
  pyautogui.hotkey('command', 'a')
  time.sleep(0.5)
  pyautogui.hotkey('command', 'v')
  # 即決価格設定
  url = url_check.url_check_t(url)
  time.sleep(0.5)
  pyautogui.moveTo(50, 720, duration=0.5)
  time.sleep(0.5)
  pyautogui.click()
  time.sleep(0.5)
  pyautogui.moveTo(50, 760, duration=0.5)
  time.sleep(0.5)
  pyautogui.click()
  decision_price = str(int(price) + 200) 
  pyperclip.copy(decision_price)
  time.sleep(0.5)
  pyautogui.hotkey('command', 'a')
  time.sleep(0.5)
  pyautogui.hotkey('command', 'v')
  logging.info('info %s %s', '商品テキスト', 'End')

  logging.info('info %s %s', '日時設定', 'Start')
  # 終了する日時
  time.sleep(0.5)
  pyautogui.vscroll(-10)
  time.sleep(0.5)
  pyautogui.moveTo(50, 540, duration=0.5)
  time.sleep(0.5)
  pyautogui.click()
  time.sleep(0.5)
  pyautogui.moveTo(50, 490, duration=0.5)
  time.sleep(0.5)
  pyautogui.click()
  logging.info('info %s %s', '日時設定', 'End')


  logging.info('info %s %s', 'メインページバック', 'Start')
  time.sleep(0.5)
  pyautogui.vscroll(3000)
  time.sleep(0.5)
  pyautogui.moveTo(80, 160, duration=0.5)
  time.sleep(0.5)
  pyautogui.click()

  time.sleep(2)
  url = url_check.url_check_f(url)
  pyautogui.moveTo(570, 170, duration=0.5)
  time.sleep(5)
  pyautogui.click()
  time.sleep(0.5)
  pyautogui.hscroll(-3000)
  time.sleep(0.5)
  pyautogui.moveTo(740, 220, duration=0.5)
  time.sleep(0.5)
  pyautogui.click()
  url = url_check.url_check_f(url)
  logging.info('info %s %s', 'メインページバック', 'End')
