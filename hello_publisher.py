#!/usr/bin/env python3
import time
import zmq
impot random

def read_ultrasonic_sensor():
  reading = random.uniform(0.05, 150.0)
  return reading

def publish_to_server():
  PORT = 5555
  context = zmq.Context()
  publisher = context.socket(zmq.PUB)
  publisher.bin(tcp://192.168.0.59:" + str(PORT))
  
  while True:
       distance = read_ultrasonic_sensor()
       msg = "\n----------------------------\n The distance to object is {:.2f} cm!\n----------------------------\n".format(distance)
       publisher.send_multipart([b"A", b" The distance to object is:"])
       publisher.send_string(msg)
       time.sleep(2)
 
  publisher.close()
  context.term()
        
if __name__ == '__main__':
      try:
          publish_to_server()
      
      except (KeyboardInterrupt, SystemExit):
           print(" User has stopped program.")
