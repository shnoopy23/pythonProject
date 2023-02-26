def sort_puzirek(numbers_list_mod):
    for i in range(len(numbers_list_mod)):
        for j in range(len(numbers_list_mod) - i - 1):
            if numbers_list_mod[j] > numbers_list_mod[j + 1]:
                numbers_list_mod[j], numbers_list_mod[j + 1] = numbers_list_mod[j + 1], numbers_list_mod[j]
    return numbers_list_mod


def binary_search(numbers_list_mod, numbers_user, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if numbers_list_mod[middle] == numbers_user:
        return middle
    elif numbers_user < numbers_list_mod[middle]:
        return binary_search(numbers_list_mod, numbers_user, left, middle - 1)
    else:
        return binary_search(numbers_list_mod, numbers_user, middle + 1, right)

what = True
while what:
    try:
        numbers_list = input("Введите последовательность натуральных чисел через пробел: ").split()



        numbers_list_mod = [int(x) for x in numbers_list]

        numbers_list_mod = sort_puzirek(numbers_list_mod)
        print('после сортировки методом пузырек:', numbers_list_mod)

        numbers_user = input("Введите число для определения индекса: ")
        numbers_user = int(numbers_user)
        what = False
    except ValueError:
            print(f'Ошибка {ValueError}')
            print('Введено недопустимое значение.')
            what = input("Повторить ввод чисел? (+ или -): ")
            if what != '+':
                print('До свидания')
                what = False
                exit(1)
            else:
                print('В следующий раз будьте внимательнее!')

if numbers_user not in numbers_list_mod:
     print(f'Нет числа {numbers_user} среди чисел последовательности. {numbers_list_mod}')
     if numbers_user < min(numbers_list_mod):
           print(f'число {numbers_user} меньше минимального последовательности. {min(numbers_list_mod)}')
     if numbers_user > max(numbers_list_mod):
           print(f'число {numbers_user} больше максимального последовательности {max(numbers_list_mod)}')
     exit(1)

number_index = binary_search(numbers_list_mod, numbers_user, 0, len(numbers_list_mod) - 1)

print("Индекс введенного числа в списке (от 0): ", number_index)
if number_index == 0:
    print(f'число {numbers_user} первое значение в списке, следующее {numbers_list_mod[number_index + 1]}')
elif number_index == int(len(numbers_list_mod)-1):
    print(f'число {numbers_user} последнее значение в списке, предыдущее значение {numbers_list_mod[number_index-1]}')
else:
    print(f'предыдущее значение {numbers_list_mod[number_index-1]}, следующее {numbers_list_mod[number_index + 1]}')