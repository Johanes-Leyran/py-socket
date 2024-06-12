import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Server started......")
    s.bind((HOST, PORT))
    s.listen()

    conn, add = s.accept()
    with conn:
        print(f"Connection at the {add}")
        while True:
            data = conn.recv(1)
            if not data:
                break
            conn.sendall(data)
            