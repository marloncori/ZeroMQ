#!/usr/bin/env python3
from random import randint
import itertools
import logging
import time
import zmq

# it works similarly to the hello_server
# it echoes request as-is, randomly runs slowly or exits to simulate a crash
logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)

context = zmq.Context()
server = context.socket(zmq.REP)
server.bind("tcp://*:5555")

for cycles in itertools.count():
    request = server.recv()
    
    # simulate various problems after a few cycles
    if cycle > 4 and randint(0, 4) == 0:
        logging.info(" Let us simulate a server crash!")
        break
    elif cycles > 4 and randint(0, 4) == 0:
        logging.info(" Now let us simulate a CPU overload...")
        time.sleep(3)
        
   logging.info(" Normal request (%s)", request)
   time.sleep(1)
   server.send(request)
