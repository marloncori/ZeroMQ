#!/usr/bin/env python3
import sys
import time
import zmq
from random import choice

#uses REQ socket to query one or more services
REQ_TIMEOUT = 1000 # milliseconds
MAX_RETRIES = 3 

def try_request(context, endpoint, request):
   print( "Trying echo service at {}...".format(endpoint))
   client = context.socket(zmq.REQ)
   client.setsockopt(zmq.LINGER, 0)
   client.connect(endpoint)
   print("[try_request] --> ", request)
   client.send_string(request)
   poll = zmq.Poller()
   poll.register(client, zmq.POLLIN)
   socks = dict(poll.poll(REQ_TIMEOUT))
   if socks.get(client) == zmq.POLLIN:
      reply = client.recv_multipart()
   else:
      reply = ''
   poll.unregister(client)
   client.close()
   return reply

cmds = [" Please turn on the robot!", " Please turn off the robot!", " Switch the leds on!", "Switch the leds off!", 
       " Move forward!", " Avoid the obstacle!", " Can you recognise this color?", " Quench the fire by enabling the water valve!",
       " Step backward!", "Take this cargo back home!", "Process LIDAR sensor readings!", " Object tracking mode activate!", " Follow me mode activate!"]
context = zmq.Context()
requet = None
reply = None

endpoints = len(sys.argv) - 1
if endpoints == 0:
    print( " --> USAGE:\n\t %s <endpoint> ..." % sys.argv[0])
elif endpoints == 1:
    endpoint = sys.argv[1]
    for retries in xrange(MAX_RETRIES):
        request = choice(cmds)
        reply = try_request(context, endpoint, request)
        print(request)
        if reply:
            break # success
        print(" WARNING: No response from %s, retrying to reach it..." % endpoint)
else:
  # for multiple endpoints, try each at most once
  for endpoint in sys.argv[1:]:
      request = choice(cmds)
      reply = try_request(context, endpoint, request)
      if reply:
         break
      print(" WARNING: No response from endpoint: %s..." % endpoint)
      
if reply:
    print(" --> Service is up and running properly!")
