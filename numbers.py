numbers = [3, 4, 5, -1, 0, 10, -20, 9, -8, 2]

three = [number for number in numbers if number%3 == 0]
print(three)
positive = [number for number in numbers if number > 0]
print(positive)
four = [number for number in numbers if number%4 != 0]
print(four)
