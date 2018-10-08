#Shachar Frank and  Eran Haim
import vigenere
import socket, time

SERVER_ADDRESS = "127.0.0.1"
SERVER_PORT = 10000
address = (SERVER_ADDRESS, SERVER_PORT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(f"Host {SERVER_ADDRESS} at port {SERVER_PORT}")
    s.connect(address)
    print("connected")
    while True:
        message = input("Enter Text: ")
        s.sendall(bytearray(vigenere.translate(message,"KeyVal","encrypt").encode()))
        data = s.recv(1024)
        print('Received', data)

