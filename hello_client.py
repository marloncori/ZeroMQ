#!/usr/bin/env python3
import time
import zmq
import random

def read_SG90_pose():
  reading = random.uniform(2.0, 180.0)
  return reading

def publish_to_server():
  PORT = 5555
  context = zmq.Context()
  publisher = context.socket(zmq.REQ)
  publisher.bin(tcp://192.168.0.59:" + str(PORT))
  counter = 1
                
  while True:
       distance = read_SG90_pose()
       msg = "\n----------------------------\n The servo motor position: {:.2f} degrees.\n----------------------------\n".format(distance)
       publisher.send_multipart([b"A", b" The distance to object is:"])
       publisher.send_string(msg)
       time.sleep(2)
       reply = publisher.recv()
       print("\n ===> Server has answered: \n\t reply #{} {}".format(counter, reply))
       counter += 1
       time.sleep(1)
 
  publisher.close()
  context.term()
        
if __name__ == '__main__':
      try:
          publish_to_server()
      
      except (KeyboardInterrupt, SystemExit):
           print(" User has stopped program.")
