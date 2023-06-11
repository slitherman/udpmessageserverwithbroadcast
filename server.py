import socket
import json

IP = "localhost"
PORT = 19999
ADDR = (IP, PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(ADDR)
client_info_list = []
rand_nums_from_broadcaster = []

while True:
    print("[STARTING SERVER...]")
    try:
        data, addr = sock.recvfrom(2048)
    except ConnectionResetError as e:
        print("Connection reset by the client")
    json_data = json.loads(data)
    try:
        age = json_data["Age"]
        if age < 0:
            feedback = f" age {age} cannot be negative please enter your aga again"
            feedback = feedback.encode("utf-8")
            sock.sendto(feedback, addr)
    except (KeyError, TypeError):
        feedback = "invalid age data or missing age input. Please try filling out the field again"
        feedback = feedback.encode("utf-8")
        sock.sendto(feedback, addr)
    print(f"received data: {data}")
    client_info_list.append(json_data)
    response_msg = f"The server just received your data: {data}"
    sock.sendto(response_msg.encode("utf-8"), addr)
    broadcast_data, broadcast_addr = sock.recvfrom(2048)
    broadcast_data_json = json.loads(broadcast_data)
    rand_nums_from_broadcaster.append(broadcast_data_json)
    print(f"received data from broadcaster: {broadcast_data_json}")
