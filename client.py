import socket
import json

# server ip
IP = "localhost"
PORT = 19999
ADDR = (IP, PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_info = {
    "name": None,
    "Age": None,
    "Sex": None,
    "Hobby": None,
}

while True:
    my_info["name"] = input("Enter your fullname")
    try:
        my_info["Age"] = int(input("Enter your age"))
        my_info["Sex"] = input("Enter your sex")
        my_info["Hobby"] = input("Enter your hobby")
    except ValueError as e:
        print("Enter a valid integer")
    sent_data = json.dumps(my_info).encode("utf-8")
    sock.sendto(sent_data, ADDR)
    recv_data, addr = sock.recvfrom(1024)
    recv_data = recv_data.decode("utf-8")
    print(recv_data)












