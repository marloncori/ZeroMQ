#!/usr/bin/env python3
import time
from random import choice
impot zmq

def configure():
  context - zmq.Context()
  socket = context.socket(zmq.REP)
  socket.bin("tcp://*:5555")
  return socket

def start_server(socket):
  reactions = [" Robot has understood it!",
      "Robot is turnig right!", " Robot is stopping...",
      "Robot is moving forward.", "Robot is moving backward.",
      "Robot is slowing down", " Robot is reading the other sensors."]

  while True:
    message = socket.recv()
    print(f"\n --> The following message has been received: \n\t{message}")
    time.sleep(1)
    socket.send_string(choice(reactions))
    time.sleep(1)

if __name__ == '__main__':
  try:
      sckt = configure()
      start_server(sckt)
      
  except (KeyboardInterrupt, SystemExit):
    print("  User has stopped program execution.")

