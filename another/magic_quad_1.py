from time import sleep

sum_column = sum_diagonal_line_one = sum_diagonal_line_two = 0

all_element_magic_array = []
magic_array = result_ = []
new_element = [0, 0, 0]
index = 1
# Генерація усіх простих чисел до 1996
list_just_number = [i for i in range(2, 1997)]

for number in list_just_number:
    while index < len(list_just_number):
        if list_just_number[index] % number == 0 and list_just_number[index] != number:
            list_just_number.pop(index)
            index -= 1
        index += 1
    index = 0

# Якщо різниця між наступним і попереднім != 2 - видалити ці елементи (400 елементів залишком)
while index < len(list_just_number) - 1:
    if list_just_number[index] - list_just_number[index - 1] == 2:
        if list_just_number[index] - 1 not in all_element_magic_array:
            all_element_magic_array.append(list_just_number[index] - 1)
    elif list_just_number[index + 1] - list_just_number[index] == 2:
        if list_just_number[index] - 1 not in all_element_magic_array:
            all_element_magic_array.append(list_just_number[index + 1] - 1)
    else:
        list_just_number.pop(index)
        index -= 1

    index += 1

# 3-вибірка із 200 (усі можливі пари елементів матриці)
for one in range(len(all_element_magic_array)):
    for two in range(len(all_element_magic_array)):
        for three in range(len(all_element_magic_array)):
            if (all_element_magic_array[one] != all_element_magic_array[two] and
                    all_element_magic_array[one] != all_element_magic_array[three] and
                    all_element_magic_array[two] != all_element_magic_array[three]):
                new_element = [
                    all_element_magic_array[one], all_element_magic_array[two], all_element_magic_array[three]
                ]
                magic_array.append(new_element)

new_array = []
all_new_array = []

print("Step one")
for array in magic_array:
    index = 0
    flag = False

    while index < len(magic_array):
        if sum(array) == sum(magic_array[index]) and array != magic_array[index]:
            new_array.append(magic_array[index])
            magic_array.pop(index)
            flag = True
            index -= 1
        index += 1
    if flag:
        new_array.append(array)
        all_new_array.append(new_array)
        new_array = []

print("Step two")

for all_array in all_new_array:
    for one in range(len(all_array)):
        for two in range(len(all_array)):
            for three in range(len(all_array)):
                if one == two or one == three or two == three:
                    continue

                if (all_array[one][0] in all_array[two] or all_array[one][0] in all_array[three] or
                        all_array[one][1] in all_array[two] or all_array[one][1] in all_array[three] or
                        all_array[one][2] in all_array[two] or all_array[one][2] in all_array[three]):
                    continue

                if (all_array[two][0] in all_array[three] or all_array[two][1] in all_array[three] or
                        all_array[two][2] in all_array[three]):
                    continue

                magic_array = [all_array[one], all_array[two], all_array[three]]

                sum_diagonal_line_one = sum_diagonal_line_two = const_sum = 0
                for column in range(len(magic_array)):
                    sum_column = 0
                    for line in range(len(magic_array)):
                        sum_column += magic_array[line][column]

                    if column == 0:
                        const_sum = sum_column

                    if sum_column != const_sum:
                        break

                    sum_diagonal_line_one += magic_array[column][column]
                    sum_diagonal_line_two += magic_array[column][2 - column]
                    if sum_diagonal_line_one != const_sum or sum_diagonal_line_two != const_sum:
                        continue

                    print(magic_array)
