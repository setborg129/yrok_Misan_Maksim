import time
from datetime import timedelta

start_time = time.time()

# print(f'Начало : {start_time}')
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]

result_src = []
result_duble = []  # список в котором будут сохранены дубликаты значений !
for item in src:
    if item not in result_src:
        result_src.append(item)
    else:
        result_duble.append(item)  # записываем дубликаты

for index, item in enumerate(result_src):
    if item in result_duble:
        result_src.remove(item)

print(result_src)


finish_time = time.time()
elapsed_time_secs = time.time() - start_time
msg = "Execution took: %s secs (Wall clock time)" % timedelta(seconds=round(elapsed_time_secs))

print(msg)
# print(f'Финиш : {finish_time}')
