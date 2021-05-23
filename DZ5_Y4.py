src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result_src = []

for index, item in enumerate(src):
    item = int(item)
    if index > 0:
        if item > src[index-1]:
            result_src.append(item)


print(result_src)