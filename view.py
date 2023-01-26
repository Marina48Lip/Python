def inp_mod():
    mod = input('Введите режим работы(импорт/экспорт): ')
    return mod


def inp_import():
    surname = input('Введите фамилию для поиска: ')
    return surname


def inp_export():
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    patronymic = input('Введите отчетство: ')
    tel_number = input('Введите номер телефона: ')
    comment = input('Введите признак телефона(мобильный/рабочий): ')
    return '\n', surname, name, patronymic, tel_number, comment


def view_import(result):
    print(*result, sep='\n')


def view_import_no():
    print(f'Данные не найдены')


def view_export(result):
    print(f'Ваши данные успешно внесены')