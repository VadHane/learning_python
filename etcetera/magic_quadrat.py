sum_line = main_number = sum_column = sum_diagonal_line = 0
flag = True

while True:
    print("Введіть ранг матриці: ->")
    SIZE_MATRIX = input()
    try:
        SIZE_MATRIX = int(SIZE_MATRIX)
    except ValueError:
        print("Виключно число! Повторіть спробу \b")
        continue

    break

magic_array = [[i for i in range(SIZE_MATRIX)] for k in range(SIZE_MATRIX)]

print("Введіть матрицю: ")
for i in range(SIZE_MATRIX):
    print("[")
    for k in range(SIZE_MATRIX):
        while True:
            try:
                magic_array[i][k] = int(input())
            except ValueError:
                print("Виключно число! Повторіть спробу \b")
                continue

            break

    print("]")

for i in range(SIZE_MATRIX):
    # Рядки
    for k in range(SIZE_MATRIX):
        sum_line += magic_array[i][k]

    if i == 0:
        main_number = sum_line

    if sum_line != main_number:
        print("False")
        flag = False

    sum_line = 0

    # Стовпці
    for k in range(SIZE_MATRIX):
        sum_column += magic_array[k][i]

    if sum_column != main_number:
        print("False")
        flag = False

    sum_column = 0

    if not flag:
        break

# Діагоналі
for i in range(SIZE_MATRIX):
    sum_diagonal_line += magic_array[i][i]

if sum_diagonal_line != main_number and flag:
    print("False")
    flag = False

sum_diagonal_line = 0

for i in range(SIZE_MATRIX):
    sum_diagonal_line += magic_array[i][SIZE_MATRIX - i - 1]

if sum_diagonal_line != main_number and flag:
    print(False)
    flag = False

if flag:
    print("It is magic :)")
