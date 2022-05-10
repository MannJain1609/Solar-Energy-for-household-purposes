import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

#servo motor-> duty cycle=(2+angle/18)

GPIO.setup(11,GPIO.OUT)
servo1=GPIO.PWM(11,50)
servo1.start(0)
time.sleep(2)

#rotating servo to 180 from 0 in 10 cycles.

while(duty<=12):
    servo1.ChangeDutyCycle(duty)
    time.sleep(1)
    duty=duty+1

time.sleep(2)


"""
import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization
try:
  while True:
    p.ChangeDutyCycle(5)
    time.sleep(2)
    p.ChangeDutyCycle(7.5)
    time.sleep(2)
    p.ChangeDutyCycle(10)
    time.sleep(2)
    p.ChangeDutyCycle(12.5)
    time.sleep(2)
    p.ChangeDutyCycle(10)
    time.sleep(2)
    p.ChangeDutyCycle(7.5)
    time.sleep(2)
    p.ChangeDutyCycle(5)
    time.sleep(2)
    p.ChangeDutyCycle(2.5)
    time.sleep(2)
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
  """