# 3 Задача
s_test = {}
result = {}
def thesaurus(*args):
    s_test = args
    s_test = list(s_test)
    s_test.sort()
    print(s_test)
    for item in s_test:
        name = result.get(item[0])
        if name == None:
            result[item[0]] = item
        else:
            name_list = f'{name}, {item} '
            result[item[0]] = [name_list]

    print(result)
    print(type(result))
thesaurus("Мария", "Иван", "Юлия", "Максим")