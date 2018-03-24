import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

pwm_servo = GPIO.PWM(18, 50)
pwm_servo.start(8.4)

GPIO.output(23, 1)
time.sleep(3)
pwm_servo.start(10)
time.sleep(3)
pwm_servo.start(8.4)
time.sleep(5)
GPIO.output(23, 0)
GPIO.cleanup()
