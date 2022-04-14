import time
import zmq

def subscribe():
  context = zmq.Context()
  sub = context.socket(zmq.SUB)
  sub.connect("tcp://192.168.0.59:5561")
  sub.setsockopt(zmq.SUBSCRIBE, b'')
  time.sleep(1)
  
  sync_client = context.socket(zmq.REQ)
  sync_client.connect("tcp://192.168.0.59:5562")
  
  sync_client.send(b'')
  sync_client.recv()
  
  # get updates and report how naby we got
  nbr = 0
  while True:
     msg = sub.recv()
      if msg == b"END":
         break
      nbr += 1
  print(" Received {} updates!".format(nbr))
  
  if __name__ == "__main__":
    subscribe()
