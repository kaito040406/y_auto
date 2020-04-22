
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

def url_check():
  time.sleep(0.2)
  pyautogui.moveTo(200, 88, duration=0)
  time.sleep(0.2)
  pyautogui.click()
  time.sleep(0.2)
  pyautogui.click()
  time.sleep(0.1)
  pyautogui.hotkey('command', 'a')
  time.sleep(0.1)
  pyautogui.hotkey('command', 'c')
  time.sleep(0.1)
  now = pyperclip.paste()
  return now

def url_check_t(befor_url):
  time.sleep(0.2)
  pyautogui.moveTo(200, 88, duration=0)
  time.sleep(0.2)
  pyautogui.click()
  time.sleep(0.2)
  pyautogui.click()
  time.sleep(0.1)
  pyautogui.hotkey('command', 'a')
  time.sleep(0.1)
  pyautogui.hotkey('command', 'c')
  time.sleep(0.1)
  now = pyperclip.paste()
  if now == befor_url:
    return now
  else:
    print("問題が発生しました。")
    sys.exit()

def url_check_f(befor_url):
  time.sleep(0.2)
  pyautogui.moveTo(200, 88, duration=0)
  time.sleep(0.2)
  pyautogui.click()
  time.sleep(0.2)
  pyautogui.click()
  time.sleep(0.1)
  pyautogui.hotkey('command', 'a')
  time.sleep(0.1)
  pyautogui.hotkey('command', 'c')
  time.sleep(0.1)
  now = pyperclip.paste()
  if now != befor_url:
    return now
  else:
    print("問題が発生しました。")
    sys.exit()