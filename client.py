#Shachar Frank and  Eran Haim
import vigenere
import random
import socket, time

SERVER_ADDRESS = "127.0.0.1"
SERVER_PORT = 10000
address = (SERVER_ADDRESS, SERVER_PORT)


def shuffle_string(string):
    chars = list(string)
    random.shuffle(chars)
    return ''.join(chars)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(f"Host {SERVER_ADDRESS} at port {SERVER_PORT}")
    s.connect(address)
    print("connected")
    while True:
        cypher = shuffle_string('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        message = input("Enter message for server: ")
        message = vigenere.translate(message, "KeyVal", "encrypt", cypher)
        message = cypher + message
        print("encrypted message:\n", message[26:])
        print("cypher:\n", message[:26])
        #print("decrypted message:\n", vigenere.translate(message[26:], "KeyVal", "decrypt", message[:26]))
        s.sendall(bytearray(message.encode()))
        data = s.recv(1024).decode()
        print('Message from server:\n OK, Received - ', vigenere.translate(data[26:], "KeyVal", "decrypt", data[:26]))
        print("\n\n")


