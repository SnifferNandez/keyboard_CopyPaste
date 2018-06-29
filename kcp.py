import os
import sys
import time
import xerox

useIfStarts = 'keypaste'

def PressKey(KeyUnicode):
  print KeyUnicode

def PasteKeystrokes(clipboard):
  for k in clipboard:
    PressKey(k)
    #PressKey(unichr(0x12)) #Alt

recent_value = ""
while True:
  tmp_value = xerox.paste()
  if useIfStarts == tmp_value[0:len(useIfStarts)] and tmp_value != recent_value:
    recent_value = tmp_value
    PasteKeystrokes(tmp_value[len(useIfStarts):])
  time.sleep(0.1)