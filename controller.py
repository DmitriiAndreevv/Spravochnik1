from import_data import import_data
from export_data import export_data
from print_data import print_data
from search_data import search_data

def greeting():
    print("Добро пожаловать в телефонный справочник!")

def input_data():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    brith_name = input("Введите дату рождения: ")
    phone_number = input("Введите номер телефона: ")
    note = input("Введите категорию контакта: ")
    return [last_name, first_name, middle_name, brith_name, phone_number, note]

def choice_sep():
    sep = input("Введите разделитель: ")
    if sep == "":
        sep = None
    return sep

def choice_todo():
    print("Выберете команду:\n\
    1 - ипорт;\n\
    2 - экспорт;\n\
    3 - поиск контакта.")
    ch = input("Введите цифру: ")
    if ch == '1':
        sep = choice_sep()
        import_data(input_data(), sep)
    elif ch == '2':
        data = export_data()
        print_data(data)
    else:
        word = input("Введите данные для поиска: ")
        data = export_data()
        item = search_data(word, data)
        if item != None:
            print('Фамилия'.center(15),'Имя'.center(15),'Отчество'.center(15),'Дата рождения'.center(15),'Телефон'.center(15),'Категория'.center(15))
            print('-'*90)
            print(item[0].center(15),item[1].center(15),item[2].center(15),item[3].center(15),item[4].center(15),item[5].center(15))
        else:
            print("Данные не обнаруженны")