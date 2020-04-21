
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

def robbot(category ,title, text, price, traffic):
  # 初期ポジ
  pyautogui.moveTo(1, 1, duration=0)
  time.sleep(0.5)
  # データの場所に行く
  pyautogui.moveTo(1000, 115, duration=0.5)
  time.sleep(0.5)
  # ここで本当はドラッグコマンド
  pyautogui.dragTo(500, 700, 1.0, button='left')
  # pyautogui.moveTo(500, 700, duration=1.0)
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
  pyperclip.copy(title)
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
  time.sleep(5)

  # カテゴリ検索へ
  pyautogui.moveTo(140, 630, duration=1.0)
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
  pyautogui.moveTo(800, 630, duration=1.0)
  time.sleep(0.5)
  pyautogui.click()
  time.sleep(0.5)

  # スクロール
  pyautogui.vscroll(-8)
  time.sleep(0.5)

  # カテゴリを選択
  pyautogui.click()
  time.sleep(0.5)
  pyautogui.moveTo(30, 585, duration=1.0)
  time.sleep(0.5)
  pyautogui.click()
  time.sleep(0.5)
  pyautogui.vscroll(-100)
  time.sleep(0.5)
  pyautogui.moveTo(550, 575, duration=1.0)
  time.sleep(0.5)
  pyautogui.click()
  time.sleep(0.5)

  # ここは少なすぎると出品に戻れなくなる
  # とりあえずは、カテゴリーふたつ検索で10個以上の列を作る
  # ドラッグしてコピーして解析できないか検査
  #  550 575
  # 一番島までスクロールさせ、上記の座標でギリギリ入る

  # 状態選択
  # pyautogui.moveTo(140, 350, duration=1.0)
  # time.sleep(0.5)
  # pyautogui.click()
  time.sleep(0.5)
  pyautogui.vscroll(-10)
  # time.sleep(0.5)
  # pyautogui.moveTo(140, 780, duration=1.0)
  # time.sleep(0.5)
  # pyautogui.click()
  # time.sleep(0.5)
  # pyautogui.moveTo(140, 650, duration=1.0)
  # time.sleep(0.5)
  # pyautogui.click()


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
  pyperclip.copy(text)
  time.sleep(0.5)
  pyautogui.hotkey('command', 'a')
  time.sleep(0.5)
  pyautogui.hotkey('command', 'v')

  # 上移動しクリックスクロール
  time.sleep(0.5)
  pyautogui.moveTo(650, 250, duration=1.0)
  time.sleep(0.5)
  pyautogui.click()
  pyautogui.vscroll(-50)


  # # 発送地域選択
  # time.sleep(0.5)
  # pyautogui.moveTo(140, 650, duration=1.0)
  # time.sleep(0.5)
  # pyautogui.click()
  # time.sleep(0.1)
  # pyautogui.vscroll(50)
  # time.sleep(0.3)
  # pyautogui.vscroll(-50)
  # time.sleep(0.3)
  # pyautogui.moveTo(140, 30, duration=1.0)
  # time.sleep(0.5)
  # pyautogui.click()
  # time.sleep(0.5)
  # pyautogui.moveTo(650, 650, duration=1.0)
  # time.sleep(0.5)
  # pyautogui.click()
  # time.sleep(0.5)


  #送料負担選択
  # pyautogui.moveTo(140, 800, duration=1.0)
  # time.sleep(0.5)
  # pyautogui.click()
  # time.sleep(0.5)
  # pyautogui.moveTo(140, 760, duration=1.0)
  # time.sleep(0.5)
  # pyautogui.click()
  # time.sleep(0.5)
  # pyautogui.moveTo(650, 650, duration=1.0)
  # time.sleep(0.5)
  # pyautogui.click()


  # # 発送方法選択
  # time.sleep(0.5)
  # pyautogui.vscroll(-26)
  # time.sleep(0.5)
  # pyautogui.moveTo(40, 660, duration=1.0)
  # time.sleep(0.5)
  # pyautogui.click()
  # time.sleep(0.5)
  # pyautogui.click()

  # #配送会社指定
  # time.sleep(0.5)
  # pyautogui.moveTo(100, 660, duration=1.0)
  # time.sleep(0.5)
  # pyautogui.click()
  # time.sleep(0.5)
  # pyautogui.vscroll(-20)
  # pyautogui.moveTo(100, 710, duration=1.0)
  # time.sleep(0.5)
  # pyautogui.click()
  # time.sleep(0.5)
  # pyautogui.moveTo(140, 710, duration=1.0)
  # time.sleep(0.5)
  # pyautogui.click()
  # pyperclip.copy(traffic)
  # time.sleep(0.5)
  # pyautogui.hotkey('command', 'a')
  # time.sleep(0.5)
  # pyautogui.hotkey('command', 'v')


  # 発送までの期間を決める
  # time.sleep(0.5)
  # pyautogui.vscroll(-10)
  # time.sleep(0.5)
  # pyautogui.moveTo(140, 500, duration=1.0)
  # time.sleep(0.5)
  # pyautogui.click()
  # time.sleep(0.5)
  # pyautogui.moveTo(140, 490, duration=1.0)
  # time.sleep(0.5)
  # pyautogui.click()
  # time.sleep(0.5)
  # pyautogui.moveTo(400, 490, duration=1.0)
  # time.sleep(0.5)


  # 値段入力
  time.sleep(0.5)
  pyautogui.moveTo(50, 670, duration=1.0)
  time.sleep(0.5)
  pyautogui.click()
  pyperclip.copy(price)
  time.sleep(0.5)
  pyautogui.hotkey('command', 'a')
  time.sleep(0.5)
  pyautogui.hotkey('command', 'v')
  # 即決価格設定
  time.sleep(0.5)
  pyautogui.moveTo(50, 720, duration=1.0)
  time.sleep(0.5)
  pyautogui.click()
  time.sleep(0.5)
  pyautogui.moveTo(50, 760, duration=1.0)
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
  pyautogui.vscroll(-10)
  time.sleep(0.5)
  pyautogui.moveTo(50, 540, duration=1.0)
  time.sleep(0.5)
  pyautogui.click()
  time.sleep(0.5)
  pyautogui.moveTo(50, 490, duration=1.0)
  time.sleep(0.5)
  pyautogui.click()
  # time.sleep(0.5)
  # pyautogui.moveTo(40, 760, duration=1.0)
  # time.sleep(0.5)
  # pyautogui.click()
  # time.sleep(0.5)
  # pyautogui.moveTo(40, 800, duration=1.0)
  # time.sleep(0.5)
  # pyautogui.click()
  # time.sleep(0.5)
  # pyautogui.moveTo(40, 760, duration=1.0)
  # time.sleep(0.5)
  # pyautogui.click()
  # time.sleep(0.5)
  # pyautogui.moveTo(400, 770, duration=1.0)
  # time.sleep(0.5)
  # pyautogui.click()


  time.sleep(0.5)
  pyautogui.vscroll(3000)
  time.sleep(0.5)
  pyautogui.moveTo(80, 160, duration=1.0)
  time.sleep(0.5)
  pyautogui.click()

  time.sleep(0.5)
  pyautogui.moveTo(570, 170, duration=1.0)
  time.sleep(10)
  pyautogui.click()
  time.sleep(0.5)
  pyautogui.hscroll(-3000)
  time.sleep(0.5)
  pyautogui.moveTo(740, 220, duration=1.0)
  time.sleep(0.5)
  pyautogui.click()
