#Shachar Frank and  Eran Haim

import vigenere #import the function class
import socket   #import the socket lbrary

#the server connection information
SERVER_ADDRESS = "localhost"
SERVER_PORT = 10000
address = (SERVER_ADDRESS, SERVER_PORT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #open's a new socket for IP\TCP and close's it after the end of the code
    print(f"server {SERVER_ADDRESS} at port {SERVER_PORT}")     #print's the server information
    s.bind(address)     #reserve the port for the adress of the server
    print("Ready!")
    s.listen(1) #the server will wait for a connection request in the port
    conn, address = s.accept()  #the server will create a connection to the adress asking  to connect
    with conn:  #creates an individual connection and close's it after code ends
        print("Connection from:", address) #connection origin
        while True:
            data = conn.recv(1024).decode() #the data from the connection
            print('encrypted data: ', data[26:])    #print the data
            print("cypher:\n", data[:26])   #print the cypher used
            print('Received: ', vigenere.translate(data[26:],"KeyVal","decrypt",data[:26])) # print translated message
            print("waiting for data\n\n")   # connection put on standby
            if not data:
                break
            conn.sendall(data.encode())
