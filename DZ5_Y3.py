tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def two_list():
    len_tutors = len(tutors)
    len_classes = len(klasses)
    for i in range(len_tutors):
        if len_classes > i:
            yield (tutors[i] + ": ", klasses[i])
        else:
            yield (tutors[i] + ": ", 'None')


gen_list = two_list()

print(gen_list)
print(type(gen_list))

