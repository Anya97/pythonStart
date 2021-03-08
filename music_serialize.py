import json
import pickle

my_favourite_group = {'name':'Би-2', 'tracks': ['Черное солнце', 'Вечная', 'Детство', 'Философский камень', 'Родина']}
print(type(my_favourite_group))

bytes_pic = pickle.dumps(my_favourite_group)
bytes_js = json.dumps(my_favourite_group)
#json_my_favourite_group = json.dumps(my_favourite_group)
#print(type(json_my_favourite_group))

with open('group.json', 'w', encoding = 'utf-8') as f:
    json.dump(my_favourite_group, f)
print('Объект в файл group.json записан')

with open('group.pickle', 'wb') as f:
    pickle.dump(my_favourite_group, f)
print('Объект в файл group.pickle записан')
