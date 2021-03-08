box = ['applles', 'pears', 'grapes', 'bananas', 'plums']
basket = ['oranges', 'applles', 'grapefruits', 'pears']

bowl = [i for i in box if i in basket]
print(bowl)
