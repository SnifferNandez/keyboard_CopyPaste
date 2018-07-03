import time
import xerox
import threading

useIfStarts = 'keypaste'
timeToKeystrokes = 5 # Time between trigger and generate keystrokes events
secs_between_keys = 0.05 # Use 0 if not want to send key by key
setMultiThread = False
sleepTime = 1 # Time between every clipboard verification
usePyautogui = False # Select method to use for keystroke

if usePyautogui:
  from pyautogui import typewrite, press
  keystroke = press
  keystrokes = typewrite
else:
  import keyboard
  keystroke = keyboard.send
  keystroke = keyboard.write # Use write instead send avoid some char issues
  keystrokes = keyboard.write

def welcome():
  print "Waiting for changed clipboard, starts with '%s'. Use CTRL+C to stop." % useIfStarts
  xerox.copy(u'Keyboard Paste as typing active :)')

def bye():
  print ' Bye'
  xerox.copy(u'Keyboard Paste as typing inactive :(')

def PressKey(key):
  if False and not usePyautogui and key in "ABCDEFGHIJKLMNOPQRSTUVWXYZ=":
    key = 'shift+' + key # Usefull when keystroke = keyboard.send
  keystroke(key)

def PasteKeystrokes(clipboard):
  print 'Clipboard detected, writing on %s seconds' % timeToKeystrokes
  time.sleep(timeToKeystrokes)
  if secs_between_keys == 0:
    keystrokes(clipboard)
  else:
    for key in clipboard:
      PressKey(key)
      time.sleep(secs_between_keys)
  print 'End of writing'

def simpleMain():
  try:
    recent_value = ""
    while True:
      tmp_value = xerox.paste()
      if useIfStarts == tmp_value[0:len(useIfStarts)] and tmp_value != recent_value and len(tmp_value) > len(useIfStarts):
        recent_value = tmp_value
        PasteKeystrokes(tmp_value[len(useIfStarts):])
      time.sleep(sleepTime)
  except KeyboardInterrupt:
    bye()

# Beggin of multithread
def ClipboardTrigger(clipboard_content):
  PasteKeystrokes(clipboard_content[len(useIfStarts):])

def CheckClipboardTrigger(clipboard_content):
  if clipboard_content.startswith(useIfStarts) and len(clipboard_content) > len(useIfStarts):
    return True
  return False

class ClipboardWatcher(threading.Thread):
  def __init__(self, predicate, callback, pause=5.):
    super(ClipboardWatcher, self).__init__()
    self._predicate = predicate
    self._callback = callback
    self._pause = pause
    self._stopping = False
  def run(self):    
    recent_value = ""
    while not self._stopping:
      tmp_value = xerox.paste()
      if tmp_value != recent_value:
        recent_value = tmp_value
        if self._predicate(recent_value):
          self._callback(recent_value)
      time.sleep(self._pause)
  def stop(self):
    self._stopping = True

def main():
  watcher = ClipboardWatcher(CheckClipboardTrigger, 
                ClipboardTrigger,
                sleepTime)
  watcher.start()
  while True:
    try:
      time.sleep(sleepTime)
    except KeyboardInterrupt:
      watcher.stop()
      bye()
      break
# End of multithread 

welcome()
if setMultiThread and __name__ == "__main__":
  main()
else:
  simpleMain()
