#!/usr/bin/env python3
import zmq

SUBSCRIBERS_EXPECTED = 10

def publish():
  context = zmq.Context()
  #socket to talk to clients
  publisher = context.socket(zmq.PUB)
  publisher.sndhwm = 11000000
  publisher.bind("tcp://*:5561")
  
  #socket to receive signals
  sync_service = context.socket(zmq.REP)
  sync_service.bind("tcp://*:5562")
  
  subscribers = 0
  while subscribers < SUBSCRIBERS_EXPECTED:
      # wait for synchronization request
      msg = sync_service.recv()
      # send reply
      sync_service.send(b'')
      subscribers += 1
      print(f" ---> +1 subscriber ({subscribers}/{SUBSCRIBERS_EXPECTED})")
  # broadcast exactly 1M updates followed by END
  for i in range(1000000):
     publisher.send(b"Rhubard")
  publisher.send(b"END")
  
  if __name__ == "__main__":
      publish()
