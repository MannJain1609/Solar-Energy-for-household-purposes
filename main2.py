from pysolar.solar import *  # Use for Pysolar data
from datetime import datetime  # Use for getting instant time
from pytz import timezone
import time  # Use for time calls
import RPi.GPIO as GPIO
import time

latitude = 20.593684
longitude = 78.96288
d = datetime.now(timezone("Asia/Kolkata"))
prev_alt = get_altitude(latitude, longitude, d)
prev_azi = get_azimuth(latitude, longitude, d)
prev_angle = 90
changes = [3, 5, 10, 15, -30]


def rotate_servo(prev_angle, change):
    GPIO.setmode(GPIO.BCM)

    # servo motor-> duty cycle=(2+angle/18)

    GPIO.setup(17, GPIO.OUT)
    servo1 = GPIO.PWM(17, 50)
    servo1.start(0)
    time.sleep(5)
    # rotating servo to 180 from 0 in 10 cycles.
    angle = int(prev_angle + change)
    prev_angle = prev_angle + change
    duty = (angle - 21 + 2) / 18
    servo1.ChangeDutyCycle(duty)
    time.sleep(2)
    return prev_angle


j = 0
for i in range(0, 40):
    d = datetime.now(timezone("Asia/Kolkata"))  # want to call this to update sun position
    curr_alt = get_altitude(latitude, longitude, d)  # current altitude
    curr_azi = get_azimuth(latitude, longitude, d)  # current azimuth
    print(curr_azi - prev_azi)
    prev_angle = rotate_servo(prev_angle, changes[j])
    j = j + 1
    prev_azi = curr_azi
    prev_alt = curr_alt
    time.sleep(30) // 900





