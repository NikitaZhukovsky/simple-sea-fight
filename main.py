from art import tprint

tprint("GamePy")

first_pole = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              ]

second_pole = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               ]

default_ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]


def choice(counter):
    state = True
    while counter <= 2:
        while state:
            ship = input("Введит тип корабля (4, 3, 2, 1): ")
            if ship.isdigit() and (ship in ['1', '2', '3', '4']):
                ship = int(ship)
                state = False
            else:
                print("Ошибка ввода!")
                continue
        state = True
        if ship in default_ships:
            while state:
                ship_orientation = input('Для вертикальной ориентации введите - 1, для горизонтальной  - 2: ')
                if ship_orientation.isdigit() and (ship_orientation == "1" or ship_orientation == "2"):
                    ship_orientation = int(ship_orientation)
                    state = False
                else:
                    print("Ошибка ввода!")
                    continue
            ship_vert = int(input('Введите номер столбца для строение корабля: '))
            ship_gor = int(input('Введите номер строки для строение корабля: '))
            counter += 1
            return ship, ship_vert, ship_gor, ship_orientation
        else:
            print("Такого корабля больше нет")
            continue
    print("Корабли закончились")


def boom(pole):
    attak_gor = int(input('Выберите горизонтальную координату атаки: '))
    attak_vert = int(input('Выберите вертикальную координату атаки: '))
    if pole[attak_gor][attak_vert] == '*':
        print('Ты попал!')
        pole[attak_gor][attak_vert] = "X"
    else:
        print('Ты промазал')
        pole[attak_gor][attak_vert] = "#"
    return pole


def add_ship(pole, ship_type, ships, vert, hor, orientation):
    if ship_type == 1:
        pole[hor][vert] = "*"
        ships.remove(1)
    elif ship_type == 2:
        if orientation == 1:
            for i in range(ship_type):
                pole[hor + i][vert] = "*"
        elif orientation == 2:
            for i in range(ship_type):
                pole[hor][vert + i] = "*"
        ships.remove(2)
    elif ship_type == 3:
        if orientation == 1:
            for i in range(ship_type):
                pole[hor + i][vert] = "*"
        elif orientation == 2:
            for i in range(ship_type):
                pole[hor][vert + i] = "*"
        ships.remove(3)
    elif ship_type == 4:
        if orientation == 1:
            for i in range(ship_type):
                pole[hor + i][vert] = "*"
        elif orientation == 2:
            for i in range(ship_type):
                pole[hor][vert + i] = "*"
        ships.remove(4)

    return pole


def print_pole(matrix):
    for row in matrix:
        print(row)


def check_health(pole):
    for i in range(10):
        if "*" in pole[i]:
            return False
    return True


counter_ship = 1

print("Игрок №1, расставьте корабли")
while counter_ship <= 2:
    first_ship, first_vert, first_hor, first_orientation = choice(counter_ship)
    first_inventory = default_ships.copy()
    print(f"Оставшиеся корабли: {first_inventory}")
    first_pole = add_ship(first_pole, first_ship, first_inventory, first_vert, first_hor, first_orientation)
    print_pole(first_pole)
    counter_ship += 1

print("\n" * 50)

counter_ship = 1
print("Игрок №2, расставьте корабли")
while counter_ship <= 2:
    second_ship, second_vert, second_hor, second_orientation = choice(counter_ship)
    second_inventory = default_ships.copy()
    print(f"Оставшиеся корабли: {second_inventory}")
    second_pole = add_ship(second_pole, second_ship, second_inventory, second_vert, second_hor, second_orientation)
    print_pole(second_pole)
    counter_ship += 1

while not (check_health(first_pole) or check_health(second_pole)):
    print("Игрок №1 стреляет")
    second_battle_pole = boom(second_pole)
    print_pole(second_battle_pole)
    print("\n" * 50)

    print("Игрок №2 стреляет")
    first_battle_pole = boom(first_pole)
    print_pole(first_battle_pole)


