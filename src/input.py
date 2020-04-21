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
import csv
import random
import string
import robbot

check = True
title_ng = 0
text_ng = 0
i = 1
k = 0
with open("input.csv") as f:
  reader = csv.reader(f)
  with open("NG_WORD.csv") as ngw:
    readerng = csv.reader(ngw)
    for row in reader:
      search_ct = row[0]
      title = row[1]
      text = row[2]
      price = row[3]
      traffic = row[6]
      # --------------------
      # バリテーション 機能
      for ng in readerng:
        if ng[0] in title:
          check = False
          title_ng  = title_ng  + 1
        if ng[0] in text:
          check = False
          text_ng  = text_ng  + 1
        k = k + 1
      #-----------------------

      if check == True:
        try:
          try:
            y_title = title[0:50]
          except IndexError:
            
            y_title = title
          y_cate = search_ct
          y_text = text
          y_price = str(price)
          y_traffic = str(traffic)
          # -------------------
          # 画像データを引っ張ってくる
          target_dir = 'images/active'
          time.sleep(1)
          shutil.rmtree(target_dir)
          os.mkdir(target_dir)
          time.sleep(1)
          sPopulation = string.ascii_lowercase + string.ascii_uppercase
          image_name = ''.join(random.sample(sPopulation,10))
          shutil.copyfile('images/stock/image' + str(i) + ".jpg", 'images/stock/' + image_name + ".jpg")
          time.sleep(0.5)
          new_path = shutil.move('images/stock/' + image_name + ".jpg", 'images/active/')
          time.sleep(1)

          #--------------------
          #ここからロボットへデータを渡す
          robbot.robbot(y_cate, y_title, y_text, y_price, y_traffic)          
          #--------------------

          # -------------------
        except FileNotFoundError:
          print("画像がなくなりました")
          break
        
      i = i + 1
      check = True
    ngw.close()
  f.close()
print(title_ng)
print(text_ng)
      
