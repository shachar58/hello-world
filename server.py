#Shachar Frank and  Eran Haim
import vigenere
import socket

#Server connectivity details
SERVER_ADDRESS = "localhost"
SERVER_PORT = 10000
address = (SERVER_ADDRESS, SERVER_PORT)
sessionIndex=0

#open socket to listen to appropriate services
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(f"server {SERVER_ADDRESS} at port {SERVER_PORT}")
    s.bind(address)
    print("Ready!")
    s.listen(1)
    conn, address = s.accept()
    #Received connection
    with conn:
        print("Connection from:", address)
        while True:
            data = conn.recv(1024).decode()             #decode the message
            print("server session",sessionIndex)
            print("encrypted message:\n",data)
            print("decrypted message:\n",vigenere.translate(data,"KeyVal","decrypt",sessionIndex))       #decrypt the data and print to screen
            print("waiting for data")
            if not data:
                break
            conn.sendall(data.encode())         #sending back encrypted data to client
            sessionIndex+=1
