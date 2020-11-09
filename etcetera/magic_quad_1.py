from time import sleep

all_element_magic_array = []
magic_array = result_ = []
new_element = [0, 0, 0]
index = 1
list_just_number = [i for i in range(1997) if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i != 1 and i != 7]


sum_column = sum_diagonal_line_one = sum_diagonal_line_two = 0

while index < len(list_just_number) - 1:
    if (list_just_number[index] - list_just_number[index - 1] == 2 or
            list_just_number[index + 1] - list_just_number[index] == 2):
        pass
    else:
        list_just_number.pop(index)
        index -= 1

    index += 1

for index in range(1, len(list_just_number), 2):
    all_element_magic_array.append(list_just_number[index] - 1)

list_just_number = list(all_element_magic_array)


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

while index < len(all_element_magic_array):
    for number in all_element_magic_array[index]:
        if number not in list_just_number:
            all_element_magic_array.pop(index)
            index -= 1
            break

    index += 1

index = 0


# while index < len(all_element_magic_array):
#     if (all_element_magic_array[index][0] == all_element_magic_array[index][1] or
#             all_element_magic_array[index][0] == all_element_magic_array[index][2] or
#             all_element_magic_array[index][1] == all_element_magic_array[index][2]):
#         all_element_magic_array.pop(index)
#         index -= 1
#     index += 1

# тут буде генерація матриць
for one in range(len(magic_array)):
    for two in range(len(magic_array)):
        for three in range(len(magic_array)):
            if one == two or one == three or two == three:
                continue
            result_ = [magic_array[one], magic_array[two], magic_array[three]]
            sum_diagonal_line_one = sum_diagonal_line_two = const_sum_column = 0
            for i in range(len(result_)):
                for k in range(len(result_)):
                    sum_column += result_[k][i]
                    if k == 0:
                        const_sum_column = sum_column

                if sum_column != const_sum_column:
                    sum_column = 0
                    break

                sum_diagonal_line_one += result_[i][i]
                sum_diagonal_line_two += result_[i][2 - i]
                if sum_diagonal_line_one != const_sum_column or sum_diagonal_line_two != const_sum_column:
                    continue

                print(
                    magic_array[one], magic_array[two], magic_array[three]
                )
