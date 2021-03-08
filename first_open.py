f = open('first.txt', 'w')

f.write('Hello\n')
f.write('World\n')

f.writelines(['Hello\n', 'Python\n'])
#for i in f:
#    print(i)
#f.close()

#with open('first.txt', 'w') as f:
#    for line in f:
#        print(line.replace('\n', ''))

#print('end')
