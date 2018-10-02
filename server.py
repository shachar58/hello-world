import socket, pickle
from User import User

SERVER_ADDRESS = "localhost"
SERVER_PORT = 10000

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = (SERVER_ADDRESS,SERVER_PORT)
print(f"server {SERVER_ADDRESS} at port {SERVER_PORT}")
handler.bind(address)
handler.listen(1)

while True:
    print("wating for connection")