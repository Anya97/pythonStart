import random

def random_element(lst):
    if len(lst) != 0:
        return random.choice(lst)

if __name__ == '__main__':
    print(random_element([1, 2, 3, 4, 5]))
    print(random_element([]))
