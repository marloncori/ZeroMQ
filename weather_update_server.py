import zmq
from random import randrange
from time import sleep

PORT = 5556
context = zmq.Context()
socket = context.socket(zqm.PUB)
socket.bin("tcp://*:" + str(PORT))

while True:
  zipcode = randrange(1, 44100)
  temperature = randrange(-80, 135)
  humidity = randrange(10, 70)
  
  socket.send_string(f"{zipcode} {temperature} {humidity}")
  sleep(1)
