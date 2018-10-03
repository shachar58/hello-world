import socket

SERVER_ADDRESS = "localhost"
SERVER_PORT = 10000
address = (SERVER_ADDRESS, SERVER_PORT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(f"server {SERVER_ADDRESS} at port {SERVER_PORT}")
    s.bind(address)
    print("Ready!")
    s.listen(1)
    conn, address = s.accept()
    with conn:
        print("Connection from:", address)
        while True:
            data = conn.recv(1024)
            print(data)
            print("waiting for data")
            if not data:
                break
            conn.sendall(data)