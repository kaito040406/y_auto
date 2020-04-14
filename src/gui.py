##PyAutoGUIのモジュール
import pyautogui

##プロセスを制御するためにOS周りのモジュール
import re
import os
import subprocess
import sys
import time
import array

#MacやLinuxの場合は、↑３つの代わりに
import re
import subprocess

# from subprocess import Popen, PIPE
# cmd = "xwininfo -name (ウインドウ名)"
# p = Popen(cmd.split(' '),stdout = PIPE, stderr = PIPE)
# ret = str(p.communicate())
# coord = re.search('X:\s+(\d+)[^Y]+Y:\s+(\d+)',ret)
# appwin_x,appwin_y = coord.groups()

pyautogui.moveTo(1, 1, duration=1)
time.sleep(0.5)
screen_x,screen_y = pyautogui.size()
pyautogui.moveRel(1370, 40, 1)
time.sleep(0.5)
pyautogui.dragTo(400, 400, 1, button='left')