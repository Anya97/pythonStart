import random

def game(a, b):
#    a = 1
#    b = 100
    rand = random.randint(a,b)
    print(rand)
    sign = input()
    while sign == '<' or sign == '>':
        if sign == '<':
            rand -= 1
            rand = random.randint(a,rand)
            print(rand)
            sign = input()
        else:
            rand += 1
            rand = random.randint(rand,b)
            print(rand)
            sign = input()
    else:
        if sign == '=':
            print(rand)

if __name__ == '__main__':
    game(1, 100)
