#Shachar Frank and  Eran Haim
import vigenere
import socket, time

SERVER_ADDRESS = "127.0.0.1"
SERVER_PORT = 10000
address = (SERVER_ADDRESS, SERVER_PORT)
sessionIndex=0

#open socket to listen to appropriate services
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(f"Host {SERVER_ADDRESS} at port {SERVER_PORT}")
    #connect to server
    s.connect(address)
    print("connected")
    while True:
        message = input("Enter Text: ")
        s.sendall(bytearray(vigenere.translate(message,"KeyVal","encrypt",sessionIndex).encode()))       #sending encrypted message
        data = s.recv(1024).decode()
        print('Received', vigenere.translate(data,"KeyVal","decrypt",sessionIndex))
        sessionIndex += 1

