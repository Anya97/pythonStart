def number(n):
    if n == 13:
        raise ValueError ('Несчастливое число')
    else:
        return n*n

n = int(input('Введите число'))

try:
    result = number(n)

except ValueError:
    print('У нас несчастливое число')
else:
    print(result)

