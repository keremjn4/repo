from network import start_host, join_game

choice = input("""
1 - Host Game
2 - Join Game

> """)

if choice == "1":

    connection = start_host()

    connection.send("Hello from host".encode())

elif choice == "2":

    ip = input("Host IP: ")

    connection = join_game(ip)

    message = connection.recv(1024).decode()

    print(message)