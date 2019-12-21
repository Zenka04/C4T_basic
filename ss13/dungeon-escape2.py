import random
def print_board(arr):
    for m in arr:
        for n in m:
            print(n, end=' ')
        print()

arr = [['_', '_', '_', '_'],
        ['_', '_', '_', '_'],
        ['_', '_', '_', 'E'], 
        ['_', 'K', '_', '_']]

key_checker = 0
key = [4,3]
player = [0,0]
move = ('W', 'A', 'S', 'D')
while True:
    arr[player[0]][player[1]] = 'P'
    print_board(arr)
    move = input("nuoc di  ")
    move = move.upper()
    if move == 'S':
        arr[player[0]][player[1]] = '_'
        if (player[0] + 1 < len(arr)):
            player[0] += 1
            if arr[player[0]][player[1]] == 'K':
                print("ban da tim thay chia khoa")
                key_checker += 1
            if arr[player[0]][player[1]] == 'E':
                if key_checker == 1:
                    print("hoan thanh")
                    break

    elif move == 'D':
        arr[player[0]][player[1]] = '_'
        if player[1] + 1 < len(arr):
            player[1] += 1
            if arr[player[0]][player[1]] == 'K':
                print("ban da tim thay chia khoa")
                key_checker += 1
            if arr[player[0]][player[1]] == 'E':
                if key_checker == 1:
                    print("hoan thanh")
                    break

    elif move == 'W':
        arr[player[0]][player[1]] = '_'
        if player[0] - 1 >= 0:
            player[0] -= 1
            if arr[player[0]][player[1]] == 'K':
                print("ban da tim thay chia khoa")
                key_checker += 1
            if arr[player[0]][player[1]] == 'E':
                if key_checker == 1:
                    print("hoan thanh")
                    break

    elif move == 'A':
        arr[player[0]][player[1]] = '_'
        if player[1] - 1 >= 0:
            player[1] -= 1
            if arr[player[0]][player[1]] == 'K':
                print("ban da tim thay chia khoa")
                key_checker += 1
            if arr[player[0]][player[1]] == 'E':
                if key_checker == 1:
                    print("hoan thanh")
                    break
