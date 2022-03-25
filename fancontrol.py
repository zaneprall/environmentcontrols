import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(2,GPIO.OUT)
GPIO.output(2,GPIO.HIGH)

var=1

while var==1 :
  print ("Fan Starting for 2 minutes")
  print ("start : %s" % time.ctime())
  GPIO.output(2, True)
  time.sleep(5)
  print ("Fan Stopping for 1 hour")
  print ("Stop : %s" % time.ctime())
  GPIO.output(2, False)
  time.sleep(3)
