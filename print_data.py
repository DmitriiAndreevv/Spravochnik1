def print_data(data):
    if len(data) >0:
        print('Фамилия'.center(15),'Имя'.center(15),'Отчество'.center(15),'Дата рождения'.center(15),'Телефон'.center(15),'Категория'.center(15))
        print('-'*90)
        for item in data:
            print(item[0].center(15),item[1].center(15),item[2].center(15),item[3].center(15),item[4].center(15),item[5].center(15))
    else:
        print('Справочник пуст!')