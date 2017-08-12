import os
from time import sleep
import RPi.GPIO as GPIO

#--//-- GPIO initialization --//--
GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.out)


max_Temperature = 40 # The maximum temperature in Celsius after which we turn on the fan

while True:

	res = os.popen('vcgencmd measure_temp').readline()
	temp =(res.replace("temp=","").replace("'C\n",""))
	print (temp)

	if temp>max_Temperature:
		GPIO.output(4, GPIO.HIGH)
		print ("Fan on")
	else:
		GPIO.output(4, GPIO.LOW)
		print ("Fan off")

	sleep(5) 

#end


