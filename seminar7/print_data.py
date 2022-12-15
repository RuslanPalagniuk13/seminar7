def print_data(data):
    if len(data) > 0:
        print("Фамилия".center(15), "Имя".center(15), "Отчество".center(15), "Дата рождения".center(15), "Телефон".center(15), "Категория".center(20), "Дата и Время внесения".center(20))
        print("-"*130)
        for item in data:
            print(item[0].center(15), item[1].center(15), item[2].center(15), item[3].center(15), item[4].center(15), item[5].center(20), item[6].center(20))
    else:
        print("Справочник пуст!")