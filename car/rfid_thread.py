import sys
from modules.MFRC522 import MFRC522
import signal
import RPi.GPIO as gpio
import time
import threading
import requests

class rfid_thread(threading.Thread):
  def __init__(self, name):
    print('[RFID]', 'initialize')
    threading.Thread.__init__(self)
    self.name = name
    self.rfid = MFRC522()
    self.reading = True
    self.last_uid = 0
    #signal.signal(signal.SIGINT, self.end_read)
  
  def run(self):
    print('[RFID]', 'starting')
    while self.reading:
      try:
        self.read()
      except KeyboardInterrupt:
        print()
        exit(-1)
    print('[RFID]', 'stopped')
  
  def read(self):
    """
    Once the reader detect a card, emit a http request to server to make the car stop.
    """
    OK = self.rfid.MI_OK
    (status, tag_type) = self.rfid.MFRC522_Request(self.rfid.PICC_REQIDL)
    
    (status, uid) = self.rfid.MFRC522_Anticoll()
    # if have uid
    if status == OK:
      if uid != self.last_uid:
        print('[RFID]', 'Card detected')
        self.last_uid = uid
      else:
        pass
