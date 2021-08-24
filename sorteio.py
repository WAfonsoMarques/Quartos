import time
from random import randint

clients = ["Afonso", "Antonio", "Guilherme", "Laura"]
rooms = ["Quarto com mais janelas", "Quarto ao lado do quarto que tem mais janelas", "Quarto com varanda", "Quarto com candeeiro vermelho"]
rooms_with_clients = {}


def pick_rooms():
    for i in range(0, len(clients)):
        client = clients[randint(0, len(clients) - 1)]
        room = rooms[randint(0, len(rooms) - 1)]
        rooms_with_clients[client] = room
        clients.remove(client)
        rooms.remove(room)

    return rooms_with_clients


def print_raffle():
    for name, room in rooms_with_clients.items():
        print(name.upper() + " ficou com: " + room)
        time.sleep(0.5)


if __name__ == '__main__':
    for round in range(4):
        pick_rooms()
        print_raffle()
        print("\n________________NOVA RONDA________________")
        time.sleep(1)