import zmq
from msgpack import loads
import subprocess as sp
import sys
from platform import system



context = zmq.Context()
#open a req port to talk to pupil
addr = '127.0.0.1' # remote ip or localhost
req_port = "45135" # same as in the pupil remote gui
req = context.socket(zmq.REQ)
req.connect("tcp://%s:%s" %(addr,req_port))
# ask for the sub port
req.send('SUB_PORT')
sub_port = req.recv()
# open a sub port to listen to pupil
sub = context.socket(zmq.SUB)
sub.connect("tcp://%s:%s" %(addr,sub_port))
sub.setsockopt(zmq.SUBSCRIBE, 'surface')


count = 0

while True:
    

    topic,msg =  sub.recv_multipart()
    gaze_position = loads(msg)
    if len(gaze_position['gaze_on_srf']) > 0:
        name, onsrf = gaze_position['name'], (gaze_position['gaze_on_srf'][-1]['on_srf'])
        if name == "lumiere":
            if (onsrf):
                count += 1
                if count%50 == 0:
                    print ('Allumer!')
            else:
                count = 0