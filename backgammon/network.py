import socket

HOST = "0.0.0.0"
PORT = 5555


def start_host():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((HOST, PORT))
    server.listen(1)

    print("Waiting for player 2...")

    conn, address = server.accept()

    print("Player connected:", address)

    return conn


def join_game(host_ip):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((host_ip, PORT))

    print("Connected to host!")

    return client