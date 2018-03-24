import cv2
import requests

from datetime import datetime

class Camera(object):
  def __init__(self, sub_key):
    self.sub_key = sub_key # subcription key

  def recognize_frame(self, frame):
    _, img = cv2.imencode('.jpg', frame)

    # Uncomment the next line if you want to check the image captured
    # cv2.imwrite('test.jpg', frame)
    return self.handwritten_request(img.tostring())

  def recognize(self):
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    if ret: # the frame is captured successfully
      return self.recognize_frame(frame)
    else:
      return None
    cam.release()
    
  def process_request(self, req_type, url, headers=None, params=None, data=None):
    """
    helper function to make a request.
    req_type: http request type(get, post, put, delete...)
    returns: response in python json object
    Please refer to python request documentation fro hints
    """
    retries = 0
    result = None
    max_retries = 5
    while True:
      if req_type == 'get':
        res = requests.get(url, headers=headers, params=params)
      elif req_type == 'post':
        res = requests.post(url, headers=headers, params=params, data=data)
      if res.status_code == 429:
        print( "Message: %s" % ( res.json() ) )
        if retries <= max_retries: 
          time.sleep(1) 
          retries += 1
          continue
        else: 
          print( 'Error: failed after retrying!' )
          break
      else:
        print(res)
        # print( "Message: %s" % ( res.json() ) )
        result = res.json()
      break

    return result

  def handwritten_request(self, data):
    """
    data: binary string of the captured image
    TODO:
    Make use of process_request to make request to azure API URL and get the response
    Please refer to azure documentation for hint
    
    """
    return ''
    
