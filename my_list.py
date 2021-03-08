import math
def my_lst(lst):
    new_lst = [int(math.sqrt(i)) if i > 0 else int(i) for i in lst]
    return new_lst


print(my_lst([1, -3, 4]))

