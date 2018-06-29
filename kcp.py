import time
import xerox
import threading

useIfStarts = 'keypaste'
setMultiThread = False
sleepTime = 1 # Time between every clipboard verification 


def welcome():
  print "Waiting for changed clipboard, starts with '%s'. Use CTRL+C to stop." % useIfStarts
  xerox.copy(u'Keyboard Paste as typing active :)')

def bye():
  print ' Bye'
  xerox.copy(u'Keyboard Paste as typing inactive :(')

def PressKey(KeyUnicode):
  print KeyUnicode

def PasteKeystrokes(clipboard):
  print 'changed'
  for k in clipboard:
    PressKey(k)
    #PressKey(unichr(0x12)) #Alt

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
