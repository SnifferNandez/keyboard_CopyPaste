import os
import sys
import time
import xerox

useIfStarts = 'keypaste'

recent_value = ""
while True:
  tmp_value = xerox.paste()
  if useIfStarts == tmp_value[0:len(useIfStarts)] and tmp_value != recent_value:
    recent_value = tmp_value
    print "Value changed: %s" % str(recent_value)
    #UnicodeEncodeError: 'ascii' codec can't encode character u'\xb7' in position 42: ordinal not in range(128)
  time.sleep(0.1)