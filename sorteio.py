import time
from random import randint

rooms_with_clients = {}


def pick_rooms():
    clients = ["Afonso", "Antonio", "Guilherme", "Laura"]
    rooms = ["Quarto com mais janelas", "Quarto ao lado do quarto que tem mais janelas", "Quarto com varanda",
             "Quarto com candeeiro vermelho"]

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


if __name__ == '__main__':
    print("________________Inicio do sorteio________________\n")
    for round in range(4):
        rooms_with_clients.clear()
        pick_rooms()
        print_raffle()

        if round == 2:
            print("________________RONDA FINAL________________\n")
            continue
        elif round == 3:
            print("________________FIM________________\n")
            break
        print("\n________________NOVA RONDA________________\n")
        time.sleep(1)
