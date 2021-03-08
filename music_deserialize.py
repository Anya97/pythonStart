import pickle
import json

with open('group.pickle', 'rb') as f:
    result_pc = pickle.load(f)
print(result_pc)
print(type(result_pc))

with open('group.json', 'r', encoding = 'utf-8') as f:
    result_js = json.load(f)
print(result_js)
print(type(result_js))
