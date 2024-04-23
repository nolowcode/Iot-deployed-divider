from ubidots import ApiClient
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
l_led=22
#r_led=23
red=24
green=26
GPIO.setup(l_led,GPIO.OUT)
#GPIO.setup(r_led,GPIO.OUT)
GPIO.setup(red,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)
GPIO.output(red,1)
GPIO.output(green,0)
api=ApiClient(token='BBFF-Mb78Poq2nkOSzMLXC8OZubu1z2QwBu')
l_variable=api.get_variable("5ed12cdb1d84722ac7364c8b")
r_variable=api.get_variable("5ed12d9a1d84722dc9cd01fb")
while 1:
  a=l_variable.get_values(1)
  b=r_variable.get_values(1)
  if a[0]['value']:
    GPIO.output(red,0)
    GPIO.output(green,1)
    GPIO.output(l_led,1)

  else:
    GPIO.output(l_led,0)
    GPIO.output(red,1)
    GPIO.output(green,0)