import socket
import threading
import pickle
from ball import Ball

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 9999
ADDRESS = (SERVER, PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(ADDRESS)

players = [Ball(100, 100, (0, 255, 100)), Ball(300, 300, (0, 100, 255))]


def handle_clients(conn, player):
    conn.send(pickle.dumps(players[threading.active_count() - 2]))
    while True:
        players[player - 1] = pickle.loads(conn.recv(2048))

        if player == 1:
            conn.send(pickle.dumps(players[1]))
        else:
            conn.send(pickle.dumps(players[0]))


def start():
    print(f"Server is Started by {SERVER} \nWaiting for connection...")
    s.listen(2)
    player = 1
    while True:
        c, address = s.accept()
        thread = threading.Thread(target=handle_clients, args=(c, player))
        thread.start()
        print(f"Connections : {threading.active_count() - 1}")
        player += 1


start()
