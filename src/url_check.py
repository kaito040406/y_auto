
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
import logging
from line_msseage import y_auto_message
import get_api

def url_check():
  logging.info('info %s %s', 'URL取得', 'Start')
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
  logging.info('info %s %s', 'URL取得', 'End')
  return now

def url_check_t(befor_url):
  logging.info('info %s %s', 'URLチェック', 'Start')
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
    logging.info('info %s %s', 'URLチェック', 'End')
    return now
  else:
    logging.error('error %s %s', 'エラー', 'URLに異常があります')
    message = y_auto_message(get_api.get_api_token())
    message.sendmessage("2")
    sys.exit()

def url_check_f(befor_url):
  logging.info('info %s %s', 'URLチェック', 'Start')
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
    logging.info('info %s %s', 'URLチェック', 'End')
    return now
  else:
    logging.error('error %s %s', 'エラー', 'URLに異常があります')
    message = y_auto_message(get_api.get_api_token())
    message.sendmessage("2")
    sys.exit()