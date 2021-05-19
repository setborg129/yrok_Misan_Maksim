from requests import get


def valuta(text = 'USD'):
    result_text = get('http://www.cbr.ru/scripts/XML_daily.asp').text
    data_inf = result_text.find('Date')
    current_data = result_text[data_inf + 6:data_inf + 16]
    current_valuta(result_text, current_data, text)


def current_valuta(text, current_d, current='USD'):
    current = current.upper()
    data_inf_start = text.find('<CharCode>')
    data_inf2_end = text.find('</CharCode>')
    current_name = text[data_inf_start + 10: data_inf2_end]
    if current_name == current:
        nomin_inf = text.find('<Nominal>')
        nomin_inf2 = text.find('</Nominal>')
        current_nomin = text[nomin_inf + 9: nomin_inf2]
        Value_inf = text.find('<Value>')
        Value_inf2 = text.find('</Value>')
        Value = text[Value_inf + 7: Value_inf2]
        print(f'Сегодня {current_d}: Валютная пара {current_name}: номинал {current_nomin}: в RUR = {Value} ')
    else:
        data_inf = text.find('</Valute>')
        text = text[data_inf + 19:]
        if text == '':
            print(f'Валюты {current} нет в списке')
        else:
            current_valuta(text, current_d, current)
