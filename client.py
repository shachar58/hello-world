import socket, time, user

SERVER_ADDRESS = "127.0.0.1"
SERVER_PORT = 10000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = (SERVER_ADDRES,SERVER_PORT)
sock.connect(address)