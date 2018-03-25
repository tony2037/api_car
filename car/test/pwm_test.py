import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(18, gpio.OUT)
servo = gpio.PWM(18, 50)

print('Pwm test for servo. Press Ctrl+C to exit.')

while True:
  try:
    inp = float(input('Input servo: '))
    if inp < 1 or inp > 10:
      raise ValueError
    servo.start(inp)
  except KeyboardInterrupt:
    print('\nExiting...')
    gpio.cleanup()
    exit(-1)
  except ValueError:
    print('Please enter float number between 1-10')
