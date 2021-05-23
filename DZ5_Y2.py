nums_gen = (num for num in range(1, 10 + 1, 2))
print(nums_gen)
print(type(nums_gen))

for nums in nums_gen:
    print(nums)
