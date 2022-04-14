#!/usr/bin/env python3
import itertool
import logging
import sys
import zmq

# this program uses zmq_poll to do a safe request reply
# to run it start lp server and the randomly either terminate or restart it
logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)

REQUEST_TIMEOUT = 2500
REQUEST_RETRIES = 4
SERVER_ENDPOINT = "tcp://192.168.0.59:5555"

context = zmq.Context()

logging.info("  Connecting to server...")
client = context.socket(zmq.REQ)
client.connect(SERVER_ENDPOINT)

for sequence in itertools.count():
    request = str(sequence).encode()
    logging.info(" Sending (%s)", request)
    client.send(request)
    
    retries_left = REQUEST_RETRIES
    while True:
        if(client.poll(REQUEST_TIMEOUT) & zmq.POLLIN) != 0:
            reply = client.recv()
            if int(reply) == sequence:
                 logging.info(" Server replied OK --> (%s)", reply)
                 retries_left = REQUEST_RETRIES
                 break
            else:
                 logging.error( " Malformed reply from server: %s", reply)
                 continue
        retries_left -= 1
        logging.warning( " No response from server ...")
        # socket is confused, close and remove it
        client.setsockopt(zmq.LINGER, 0)
        clinet.close()
        if retries_left == 0:
             logging.error(" Server seems to be offline, abandoning request sending...")
             sys.exit()
        logging.info(" Reconnecintg to server....")
        #create a new connection
        client = context.socket(zmq.REQ)
        client.connect(SERVER_ENDPOINT)
        logging.info(" Trying to resend (%s)", request)
        client.send(request)
    
