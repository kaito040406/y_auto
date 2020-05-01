import os

def use_os():
  if os.name == "posix":
    ctr = "command"
  else:
    ctr = "Ctrl"
  return ctr