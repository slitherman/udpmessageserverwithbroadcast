import random
import socket
import json
from time import sleep

IP = "localhost"
PORT = 19999
ADDR = (IP, PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)




while True:

    rand_num = random.randint(1,100)
    rand_dict = {"num": rand_num }
    rand_num_to_json = json.dumps(rand_num).encode("utf-8")
    sock.sendto(rand_num_to_json, ADDR)
    print(rand_num_to_json)
    sleep(4)





