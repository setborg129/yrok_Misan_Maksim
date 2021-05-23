def odd_nums(n):
    for num in range(1, n + 1, 2):
        yield num


odd_to_15 = odd_nums(10)
print(type(odd_to_15))

for number in odd_to_15:
    print(number)


