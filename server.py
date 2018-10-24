#Shachar Frank and  Eran Haim
<<<<<<< HEAD
import socket
=======
>>>>>>> shachar_change

import secrets  #import the secrets module
import string   #import the string moudle
import vigenere #import the function module
import socket   #import the socket module
import random   #import the random module

def create_key(dic, iter=6, len=8):    #creates a random key made to a defualt 8 letters length, for adefault of 6 times
    for i in range(iter):   #repeats for times specified
        new_key = ''.join(secrets.choice(string.ascii_uppercase) for letter in range(len))  #create new key
        dic[i] = new_key    #add the new key

#the server connection information
SERVER_ADDRESS = "localhost"
SERVER_PORT = 10000
address = (SERVER_ADDRESS, SERVER_PORT)
keys = {}
create_key(keys)
print(keys)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:    #open's a new socket for IP\TCP and close's it after the end of the code
    print(f"server {SERVER_ADDRESS} at port {SERVER_PORT}")     #print's the server information
    s.bind(address)                                             #reserve the port for the adress of the server
    print("Ready!")
    s.listen(1)                 #the server will wait for a connection request in the port
    conn, address = s.accept()  #the server will create a connection to the adress asking  to connect
    with conn:                  #creates an individual connection and close's it after code ends
        print("Connection from:", address)  #connection origin
        num = random.randint(0,len(keys)-1) #randomize a key for the value of the encryption key
        conn.sendall(keys[num].encode())    #send the client the key
        while True:
<<<<<<< HEAD
            data = conn.recv(1024)
            print('Received: ', data)
            print("waiting for data")
            if not data:
=======
            print("waiting for data\n\n")   # connection put on standby
            data = conn.recv(1024).decode() #the data from the connection
            if not data: #the program will stop if sent an empty packet
>>>>>>> shachar_change
                break
            print('encrypted data: ', data[26:])    #print the data
            print("cypher:\n", data[:26])           #print the cypher used
            print('Received: ', vigenere.translate(data[26:],keys[num],"decrypt",data[:26])) # print translated message
            new_data = "you said: " + vigenere.translate(data[26:],keys[num], "decrypt",data[:26]) +"?" # the server alter the message
            new_data =data[:26] + vigenere.translate(new_data,keys[num], "encrypt",data[:26])
            conn.sendall(new_data.encode()) #server send the message
