# # # # 1 Задание а)

print(type(15 * 3))
print(type(15 / 3))
print(type(15 // 2))
print(type(15 ** 2))

# # print('Создаем список')
first_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#
print(first_list)
second_list = []
for_index = 1

nums = 0  # счетчик
str_lens = len(first_list)  # изначально посчитаем длину строки !
while nums < str_lens:
    # if filter(str.isdigit, first_list):
    #     first_list.pop(nums)
    #     first_list.insert(nums, '05')
    first_list.insert(for_index, '"')
    for_index += 2
    nums += 1

for index, value_list in enumerate(first_list):
    if value_list == '5':
        first_list.pop(index)
        first_list.insert(index, '05')
    if value_list == '+5':
        first_list.pop(index)
        first_list.insert(index, '+05')

print('Обновляем список')
print(first_list)  # Список тот же

for index, nums_elem in enumerate(first_list):
    if nums_elem == '"':
        continue
    elif nums_elem == '17':
        print(f'"{nums_elem}"', end=' ')
    elif nums_elem == '+05':
        print(f'"{nums_elem}"', end=' ')
    elif nums_elem == '05':
        print(f'"{nums_elem}"', end=' ')
    else:
     print(nums_elem, end=' ')

# # 4 Задание _copy
distorted_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
                  'директор аэлита']
# for occ_add_name in distorted_list:
#     name = occ_add_name.split()[-1]
#
#     print(f'Привет, {name.capitalize()}!')

for nums_list_up in distorted_list:
    print(nums_list_up.upper(), end=" ")

print(f'\n')
for nums_list_low in distorted_list:
    print(nums_list_low.lower(), end=" ")

#5 Задание

price_nums = [1, 5, 9, 57.08, 46.1, 97, 22, 33, 45, 102.1, 903, 54, 777]

def price_item(price):
    for nums in price:
        rub = int(nums // 1)
        kop = int((nums * 100) % 100)
        if len(str(kop)) < 2:
            kop = '0' + str(kop)
        print(f'{rub} руб, {kop} коп.')

price_item(price_nums)

# Cписок по возрастанию
print('\nCписок по возрастанию')
price_nums.sort()
price_item(price_nums)

print('\nОтсортированые по убыванию')
price_nums_reverse = sorted(price_nums, reverse=True)

price_item(price_nums_reverse)
# # #
# # # # Вывести цены пяти самых дорогих товаров.
print('\nВывести цены пяти самых дорогих товаров')
print(price_nums_reverse[0:5])


