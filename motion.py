import RPi.GPIO as GPIO
import time
import datetime
import os

GPIO.setmode(GPIO.BOARD)
PIR = 26
GPIO.setup(PIR, GPIO.IN)

first_turned_off = False

print "Waiting for sensor to settle"
time.sleep(2)
print "Ready"

while True:
	on_time = os.popen('python tplink-smartplug/tplink-smartplug.py -t 192.168.1.223 -c info').read()
    
    if '\"relay_state\":0' in on_time and not first_turned_off:
    	print 'Lights just turned off, entering sleep'
    	first_turned_off = True
    	time.sleep(300)
    	print 'Done sleeping'

    else:
    	first_turned_off = False

	if GPIO.input(PIR) and datetime.now().hour >= 12:
    	print "Motion Detected!"

    	os.system('python tplink-smartplug/tplink-smartplug.py -t 192.168.1.223 -c on')

    	time.sleep(2)
   	time.sleep(0.1)