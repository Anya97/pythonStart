data = '23.03.1997'
data_f = ''
if data[0] == '0':
    if data[1] == '1':
        data_f += 'первое'
    elif data[1] == '2':
        data_f += 'второе'
    elif data[1] == '3':
        data_f += 'третье'
    elif data[1] == '4':
        data_f += 'четвёртое'
    elif data[1] == '5':
        data_f += 'пятое'
    elif data[1] == '6':
        data_f += 'шестое'
    elif data[1] == '7':
        data_f += 'седьмое'
    elif data[1] == '8':
        data_f += 'восьмое'
    elif data[1] == '9':
        data_f += 'девятое'
elif data[0] == '1':
    if data[1] == '0':
        data_f += 'десятое'
    elif data[1] == '1':
        data_f += 'одинадцатое'
    elif data[1] == '2':
        data_f += 'двенадцатое'
    elif data[1] == '3':
        data_f += 'тринадцатое'
    elif data[1] == '4':
        data_f += 'четырнадцатое'
    elif data[1] == '5':
        data_f += 'пятнадцатое'
    elif data[1] == '6':
        data_f += 'шестнадцатое'
    elif data[1] == '7':
        data_f += 'семнадцатое'
    elif data[1] == '8':
        data_f += 'восемнадцатое'
    elif data[1] == '9':
        data_f += 'девятнадцатое'
elif data[0] == '2':
    if data[1] == '0':
        data_f += 'двадцатое'
    elif data[1] == '1':
        data_f += 'двадцать первое'
    elif data[1] == '2':
        data_f += 'двадцать второе'
    elif data[1] == '3':
        data_f += 'двадцать третье'
    elif data[1] == '4':
        data_f += 'двадцать четвертое'
    elif data[1] == '5':
        data_f += 'двадцать пятое'
    elif data[1] == '6':
        data_f += 'двадцать шестое'
    elif data[1] == '7':
        data_f += 'двадцать седьмое'
    elif data[1] == '8':
        data_f += 'двадцать восьмое'
    elif data[1] == '9':
        data_f += 'двадцать девятое'
elif data[0] == '3':
    if data[1] == '0':
        data_f += 'тридцатое'
    elif data[1] == '1':
        data_f += 'тридцать первое'
if data[3] == '0':
    if data[4] == '1':
        data_f += ' января '
    elif data[4] == '2':
        data_f += ' февраля '
    elif data[4] == '3':
        data_f += ' марта '
    elif data[4] == '4':
        data_f += ' апреля '
    elif data[4] == '5':
        data_f += ' мая'
    elif data[4] == '6':
        data_f += ' июня '
    elif data[4] == '7':
        data_f += ' июля '
    elif data[4] == '8':
        data_f += ' августа '
    elif data[4] == '9':
        data_f += ' сентября '
if data[3] == '1':
    if data[4] == '0':
        data_f += ' октября '
    elif data[4] == '1':
        data_f += ' ноября '
    elif data[4] == '2':
        data_f += ' декабря '
print(data_f + data[6:] + ' года')
