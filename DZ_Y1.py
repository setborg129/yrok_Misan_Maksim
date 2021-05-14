import time

# 1 ЗАДАНИЕ
result = time.gmtime(6546548)
print('\nДо минуты -', result.tm_sec, 'сек')
print(f"\nДо часа   - {result.tm_min} мин: {result.tm_sec} сек:")
print(f"\nДо суток  - {result.tm_hour} час: {result.tm_min} мин: {result.tm_sec} сек:")
print(f"\nДо месяца -  неделя {result.tm_wday}: {result.tm_hour} час: {result.tm_min} мин: {result.tm_sec} сек:")
print(f"\nДо года   -  месяц {result.tm_mday}: неделя {result.tm_wday}: {result.tm_hour} час: {result.tm_min} мин: {result.tm_sec} сек:")
print(f"\nБольше года  - Год {result.tm_year}: месяц {result.tm_mday}: неделя {result.tm_wday}: {result.tm_hour} час: {result.tm_min} мин: {result.tm_sec} сек:")


#2 Задание

summ_result_17 = 0
summ_result = 0

# Создаем пустой список
spisok_cube = [number**3 for number in range(1, 1000,2)]              #готовим список нечетных чисел в кубе

#print(f'Список кубов из нечетных чисел от {spisok_cube}')

for cube in spisok_cube:
    copy_cube = cube
    local_summ_result = 0
    while cube != 0:
        local_summ_result += cube % 10          # накапливаем сумму
        cube = cube // 10                       # выход из цикла
    if local_summ_result % 7 == 0:
        summ_result += copy_cube                # суммируем итоговую сумму

print(f'Результат суммы:           {summ_result}')

for cube in spisok_cube:
    copy_cube = cube
    local_summ_result = 0
    cube = cube + 17
    while cube != 0:
        local_summ_result += cube % 10          # накапливаем сумму
        cube = cube // 10                       # выход из цикла
    if local_summ_result % 7 == 0:
        summ_result_17 += copy_cube             # суммируем итоговую сумму

print(f'Результат суммы с доп(17): {summ_result_17}')


# 3 ЗАДАНИЕ
proc1 = " процентов"
proc2 = " процент"
proc3 = " процента"

while True:
    number_skl = int(input('Введите число от 0 до 20: '))
    if 0 <= number_skl <= 20:
        if number_skl == 0:
            print(str(number_skl) + proc1)
            break
        elif number_skl % 100 >= 10 and number_skl % 100 <= 20:         #процентов
            print(str(number_skl) + proc1)
            break
        elif number_skl % 10 == 1:                                      #процент
            print(str(number_skl) + proc2)
            break
        elif number_skl % 10 >= 2 and number_skl % 10 <= 4:             #процента
            print(str(number_skl) + proc3)
            break
    else:                                                               #процентов
        print(str(number_skl) + proc1)
