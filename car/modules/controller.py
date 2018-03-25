from RPi import GPIO as gpio
import time

class Controller(object):
  def __init__(self, motor_pin, servo_pin):
    if gpio.getmode() != gpio.BCM:
      gpio.setmode(gpio.BCM)
    self.motor = motor_pin
    gpio.setup(self.motor, gpio.OUT)
    gpio.setup(servo_pin, gpio.OUT)
    self.servo = gpio.PWM(servo_pin, 50)

    # Please replace these values below with tuned ones
    self.middle_val = 8.3
    self.left_val = self.middle_val - 1.8
    self.right_val = self.middle_val + 1.8

  def forward(self):
    gpio.outpute(self.motor, 1)
    self.servo.start(self.middle_val)

  def left(self, turn_time):
    gpio.output(self.motor, 1)
    self.servo.start(self.left_val)
    time.sleep(turn_time)
    self.servo.start(self.middle_val)

  def right(self, turn_time):
    gpio.output(self.motor, 1)
    self.servo.start(self.right_val)
    time.sleep(turn_time)
    self.servo.start(self.middle_val)

  def stop(self):
    gpio.output(self.motor, 0)

  def cleanup(self):
    gpio.cleanup()
