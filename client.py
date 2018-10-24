#Shachar Frank and  Eran Haim
<<<<<<< HEAD
import socket, time
=======
>>>>>>> shachar_change

import vigenere #import the function class
import random   #import random module
import socket   #import the socket module

#the client connection information
SERVER_ADDRESS = "127.0.0.1"
SERVER_PORT = 10000
address = (SERVER_ADDRESS, SERVER_PORT)

def shuffle_string(string): #change's the order of the alphabet string, in order to make a key(cypher)
    chars = list(string)
    random.shuffle(chars)
    return ''.join(chars)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: ##open's a new socket for IP\TCP and close's it after the end of the code
    print(f"Host {SERVER_ADDRESS} at port {SERVER_PORT}")   #print's the client information
    s.connect(address)  #connect's to the port in connection information
    key = s.recv(1024).decode()
    print("connected")
    while True:
<<<<<<< HEAD
        message = input("Enter Text: ")
        s.sendall(bytearray(message, encoding="ascii"))
        data = s.recv(1024)
        print('Sent:', data)
=======
        cypher = shuffle_string('ABCDEFGHIJKLMNOPQRSTUVWXYZ')   # the cypher function  shuffle's the alphabet into a cypher
        print("To quit, type: 'bye' ")
        message = input("Enter message for server: ")   #prompt the user to create a message
        if message == "bye":    #when the user type 'bye'the program will stop
            break
        message = vigenere.translate(message, key, "encrypt", cypher)  #encrypt the message with the KeyVal key and the randomizd cypher
        message = cypher + message                                     # combining the message with the cypher, as a 26 char pre-message data
        print("\nencrypted message:  ", message[26:])                  #prints the message from the end of the cypher to the end
        print("cypher:", message[:26])              #print only the cypher
        print("decrypted message:  ", vigenere.translate(message[26:], key, "decrypt", message[:26]),"\n")  # the message decrypted using the cypher whithin it
        s.sendall(bytearray(message.encode()))  #send's the message
        data = s.recv(1024).decode()            #recive the reply from the server
        print('Message from server:\n Server Sent - ', vigenere.translate(data[26:], key, "decrypt", data[:26]),"\n\n")   #print and decypher the message from the server

>>>>>>> shachar_change

