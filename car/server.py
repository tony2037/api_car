import sys
if len(sys.argv) != 2 or not (sys.argv[1] != 'text' or sys.argv[1] != 'speech'):
  print('Usage: python3 {} speech/text'.format(sys.argv[0]))
  exit(-1)

import RPi.GPIO as gpio
from flask import Flask
from flask import jsonify
from modules.camera import Camera
from modules.controller import Controller
from rfid_thread import rfid_thread

mode = sys.argv[1]
SUBSCRIPTION_KEY = 'fe2e8c9089114086b7c54cf36aecd23c'
if mode == 'text':
  camera = Camera(SUBSCRIPTION_KEY)

app = Flask(__name__)
controller = Controller(23, 18) # motor_pin, servo_pin

@app.route('/')
def root():
  return 'woooow'

@app.route('/forward')
def forward():
  controller.forward()
  return jsonify(success=True)

"""
TODO: 
Define API for /left, /right, /stop event
Refer the /forward example above for hint
"""

@app.route('/left')
def left():
  controller.left(1000)
  return jsonify(success=True)


@app.route('/right')
def right():
  controller.right(1000)
  return jsonify(success=True)


@app.route('/stop')
def stop():
  controller.stop()
  return jsonify(success=True)

@app.route('/rfid')
def on_rfid():
  """
  TODO: 
  Handle request from rfid.
  Speech mode:
    Nothing to do 
  CV mode:
    Camera captures image and gets command from recognized result
  """
  controller.stop()
  if mode == 'text':
    result = camera.recognize().lower().rstrip()
    cmd = result2cmd(result)
    if cmd == 'left':
      controller.left(4)
    elif cmd == 'right':
      controller.right(4)
  return jsonify(success=True)


if __name__ == '__main__':
  gpio.setmode(gpio.BCM)
  rfid = rfid_thread('makentu')
  try:
    rfid.start()
    app.run(host='0.0.0.0',port=1111, threaded=True, debug=False)
  except KeyboardInterrupt:
    print('Interrupt, Exiting...')
  finally:
    print('Exiting...')
    controller.stop()
    gpio.cleanup()
    exit(-1)

