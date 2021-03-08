import sys
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info, change_dir
from game import game

save_info('Начало')

try:
    command = sys.argv[1]
except IndexError:
    command = 'Необходимо выбрать команду help'

else:
    
    if command == 'list':
        get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название файла')
        else:
            create_folder(name)
    elif command == 'game':
            game()        
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название папки')
        else:
            create_folder(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название папки')
        else:
            delete_file(name)
    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            print('Отсутствует название файлаи и название копии')
        else:
            copy_file(name, new_name)
    elif command == 'ch':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название папки')
        else:
            change_dir(name)
    elif command == 'help':
        print('list - список функций и папок')
        print('create_file - создание файла')
        print('create_folder - создание файла')
        print('delete - удаление файла или папки')
        print('copy - копирование файла или папки')

    save_info('Конец')
