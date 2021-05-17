import random
def get_jokes(col_num):
    numbers = 0
    result = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    while numbers < col_num:
        items_word1 = random.choices(nouns)
        items_word2 = random.choices(adverbs)
        items_word3 = random.choices(adjectives)
        item_num1 = random.randrange(0, len(items_word1))
        item_num2 = random.randrange(0, len(items_word2))
        item_num3 = random.randrange(0, len(items_word3))
        result.append(f'{items_word1[item_num1]} {items_word2[item_num2]} {items_word3[item_num3]}')
        result = list(result)
        numbers += 1

    print(result)

get_jokes(3)
