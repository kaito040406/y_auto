import os, sys, time
import csv
import datetime
import eel


@eel.expose
def start(input_data):
  print(len(input_data))
  return True


eel.init("web")
web_app_options = {
  "mode":"chrome",
  "port":8000,
  'chromeFlags': ["--start-fullscreen", "--browser-startup-dialog"]
}
eel.start("index.html")