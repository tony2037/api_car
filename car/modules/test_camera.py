from camera import Camera

SUB_KEY = 'SUBSCRITION KEY HERE'

cam = Camera(SUB_KEY)
result = cam.recognize()
print('Result:')
if not result:
  print('Not detected')
else:
  print(result)
