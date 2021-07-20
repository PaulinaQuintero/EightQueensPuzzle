# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def get_solutions(n):
    board = {}
    n = int(n)
    for x in range(n):
        for y in range(n):
            box_name = "x{}y{}".format(x, y)
            board[box_name] = True
    print(board)



is_int = False
n = 0
while not is_int:
    print("N:")
    n = input()
    try:
        int(n)
        is_int = True

    except ValueError:
        print("Ese no es un numero valido")

get_solutions(n)


