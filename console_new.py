print('Консольный файловый менеджер: ')
import os
import shutil
import sys
from victorina import get_person_and_question
import pickle
import random

FILE_NAME_LISTDIR = 'listdir.txt'
file_name = []
dir_name = []

# декоратор
def frame(func):
    def inner(*args, **kwargs):
        print('*' * 30)
        result = func(*args, **kwargs)
        print('*' * 30)
        return result

    return inner

@frame
def author():
    author_name = 'Туз Любовь Ивановна'
    print(f'*   {author_name}  *')
    return

@frame
def bye_bye():
    # тернарный оператор
    good_bye = '     GOOD BYE!!       ' if random.random() > 0.5 else '    ДО СВИДАНИЯ!!    '
    print(f'*   {good_bye}  *')
    return

while True:
    print('1. создать папку')
    print('2. удалить файл/папку')
    print('3. копировать файл/папку')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории')
    print('12. сохранить содержимое рабочей директории в файл')
    print('13. выход')

    choice = input('Выберите пункт меню: ')
    if choice == '1':  # создать папку
        dir_name = input("Введите имя новой папки: ")
        # обработка исключения, если папка существует
        try:
            os.mkdir(dir_name)
        except OSError as exc:
            print(f' Ошибка!!!  {exc}')

    # выше добавлена обработка исключения try except, заменила код ниже
    # if choice == '1': # создать папку
    #     name_folder = input('Введите название папки: ')
    #     # проверка на существование
    #     if not os.path.exists(name_folder):
    #         os.mkdir(name_folder)
    #         print(f'Папка {name_folder} создана')
    #     else:
    #         print(f'Папка с именем {name_folder} уже существует')

    elif choice == '2':
        del_name = input('Введите имя удаляемого файла или папки: ')
        if os.path.isdir(del_name):  # удаляем папку
            os.rmdir(del_name)
        elif os.path.isfile(del_name):  # удаляем файл
            os.remove(del_name)
        else:
            print('Неизвестное имя')
        print(f'Папка/файл {del_name} удален(а)')

    elif choice == '3':
        copy_folder = input('Введите название файла/папки, который(ую) необходимо копировать:  ')
        new_folder = input('Введите новое название файла/папки:  ')
        if os.path.exists(copy_folder) and not os.path.exists(new_folder):
            shutil.copy(copy_folder, new_folder)

    elif choice == '4':
        print('Текущая директория: ', os.getcwd())

    elif choice == '5':  # посмотреть папки
        dirs_view = [d for d in os.listdir('.') if os.path.isdir(d)]
        print(dirs_view)

    elif choice == '6':  # посмотреть файлы
        files_view = [f for f in os.listdir('.') if os.path.isfile(f)]
        print(files_view)

    elif choice == '7':
        print('My OS is', sys.platform, '(', os.name, ')')

    elif choice == '8':
        author()

    elif choice == '9':
        rounds = int(input('Сколько раз вы хотите играть?'))

        for i in range(rounds):
            get_person_and_question()

        print('Пока!')
    elif choice == '10':
        import shop

    elif choice == '11':
        print(f'Вы находитесь {os.getcwd()}')
        new_directory = input('введите название рабочей папки: ')
        os.mkdir(new_directory)
        path = os.path.join(os.getcwd(), new_directory)
        os.chdir(path)
        print(f'А теперь вы находитесь {os.getcwd()}')

    elif choice == '12': # сохранить содержимое рабочей директории в файл
        # with open(FILE_LISTDIR, 'w', encoding='UTF-8') as f:
        #     file_names = ', '.join([ff for ff in os.listdir('.') if os.path.isfile(ff)])
        #     f.write(f'files: {file_names} \n')
        #     dir_names = ', '.join([ff for ff in os.listdir('.') if os.path.isdir(ff)])
        #     f.write(f'dirs : {dir_names}')
        content = os.listdir()
        for direct in content:
            if os.path.isdir(direct):
                dir_name.append(direct)
            if os.path.isfile(direct):
                file_name.append(direct)
        with open(FILE_NAME_LISTDIR, 'wb') as f:
            pickle.dump(dir_name, f)
            pickle.dump(file_name, f)

    elif choice == '13':
        bye_bye()
        break
    else:
        print('Неверный пункт меню')

