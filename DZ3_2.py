data_db_translate = {'one': 'один',
                     'two': 'два',
                     'three': 'три',
                     'four': 'четыре',
                     'five': 'пять',
                     'six': 'шесть',
                     'seven': 'семь',
                     'eigth': 'восемь',
                     'nice': 'девять',
                     'ten': 'десять',

                     'One': 'Один',
                     'Two': 'Два',
                     'Three': 'Три',
                     'Four': 'Четыре',
                     'Five': 'Пять',
                     'Six': 'Шесть',
                     'Seven': 'Семь',
                     'Eigth': 'Восемь',
                     'Nice': 'Девять',
                     'Ten': 'Десять',
                     }
# 2 Задача

def num_translate_adv(keys):
    result = data_db_translate.get(keys)
    print(result)

num_translate_adv("One")