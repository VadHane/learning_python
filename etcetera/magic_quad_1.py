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


for array in magic_array:
    all_element_magic_array = []
    index = 0
    flag = False

    while index < len(magic_array):
        if sum(array) == sum(magic_array[index]) and array != magic_array[index]:
            all_element_magic_array.append(magic_array[index])
            magic_array.pop(index)
            flag = True
            index -= 1
        index += 1
    if flag:
        all_element_magic_array.append(array)

    index = 0
    for one in range(len(all_element_magic_array)):
        for two in range(len(all_element_magic_array)):
            for three in range(len(all_element_magic_array)):
                if one == two or one == three or two == three:
                    continue
                result_ = [all_element_magic_array[one], all_element_magic_array[two], all_element_magic_array[three]]

                flag = False
                for array_1 in all_element_magic_array:
                    for element in array_1:
                        while index < len(all_element_magic_array):
                            if element in all_element_magic_array[index] and all_element_magic_array[index] != array_1:
                                flag = True
                                break
                            index += 1
                        if flag:
                            break
                        index = 0
                    if flag:
                        break
                if flag:
                    continue

                sum_diagonal_line_one = sum_diagonal_line_two = const_sum_column = 0
                for i in range(len(result_)):
                    sum_column = 0
                    for k in range(len(result_)):
                        sum_column += result_[k][i]

                    if i == 0:
                        const_sum_column = sum_column

                    if sum_column != const_sum_column:
                        break

                    sum_diagonal_line_one += result_[i][i]
                    sum_diagonal_line_two += result_[i][2 - i]
                    if sum_diagonal_line_one != const_sum_column or sum_diagonal_line_two != const_sum_column:
                        continue

                    print(
                        all_element_magic_array[one], all_element_magic_array[two], all_element_magic_array[three]
                    )
