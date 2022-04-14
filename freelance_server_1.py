#!/usr/bin/env python3
import sys
import zmq

# freelance server model 1 - trivial echo service
if len(sys.argv) < 2:
    print(" INFO: Syntax = \n\t %s <endpoint>\n" % sys.argv[0])
    sys.exit(0)

endpoint = sys.argv[1]
context = zmq.Context()
server = context.socket(zmq.REP)
server.bind(endpoint)

print(" INFO: Echo service is ready at %s" % endpoint)
while True:
    msg = server.recv_multipart()
    if not msg:
        break
    server.send_multipart(msg)

server.setsockopt(zmq.LINGER, 0) #terminate immediately
