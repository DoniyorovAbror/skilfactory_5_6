
win = [[1,2,3],[4,5,6],[7,8,9],[1,5,9],[1,4,7],[2,5,8],[3,6,9],[3,5,7]]

numbers = {1 : '1', 2 : '2', 3 : '3',
           4 : '4', 5 : '5', 6 : '6',
           7 : '7', 8 : '8', 9 : '9'}

def check_win():
    for i in win:
        if numbers[i[0]] == numbers[i[1]] == numbers[i[2]]:
            return True

def board(n):
    print(f' {n.get(1)} | {n.get(2)} | {n.get(3)}')
    print('-' * 11)
    print(f' {n.get(4)} | {n.get(5)} | {n.get(6)}')
    print('-' * 11)
    print(f' {n.get(7)} | {n.get(8)} | {n.get(9)}')

board(numbers)

cont = 1
player = 'X'
while True:
    if cont > 9:
        print("Все клетки заполнены игра закончилась в ничью")
        break
    if cont % 2 == 0:
        player = "O"
    else:
        player = "X"
    hint = input(f'{player} Ваш ход выберите число: ')
    if not hint.isdigit():
        print("Введите только число")
    elif int(hint) < 1 or int(hint) > 9:
        print("Такой клетки нет")
    elif numbers.get(int(hint)) == "X" or numbers.get(int(hint)) == "O":
        print("Клетка занята")
    else:
        numbers[int(hint)] = player
        if cont >= 5:
            if check_win():
                print()
                board(numbers)
                print()
                print(f'Победил игрок {player}')
                print()
                break
        cont += 1
        board(numbers)
