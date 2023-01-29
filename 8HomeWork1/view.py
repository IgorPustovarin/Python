# 1. Открыть файл
# 2. Сохранить файл
# 3. Показать все контакты
# 4. Создать контакт
# 5. Удалить контакт
# 6. Изменить контакт
# 7. Найти контакт
# 8. Выход из программы
commands = ['Открыть файл' ,
            'Сохранить файл', 
            'Показать все контакты',
            'Создать контакт',
            'Удалить контакт',
            'Изменить контакт',
            'Найти контакт',
            'Выход из программы']
def main_menu():
    print('Главное меню')
    for i, item in enumerate(commands, 1):# enumerate(commands, 1) цифра 1 указывает нумерацию с единицы
        print(f'\t{i}. {item}')
    choice = ''
    while True:
        try:############################ОЧЕНЬ НУЖНАЯ ЗАЩИТА ОТ "ДУРАКА"
            choice = int(input('Выберете пункт меню: '))
            if 0 < choice < 9:
                return choice######################ИСПОЛЬЗОВАТЬ В БУДУЩЕМ!!!!!!!!!
            else:
                print('Введите значение от 1 до 8')
        except ValueError:#################ValueError Это указание типа ошибки, когда не может первести из строки в интеджер
            print('Введите корректное число')
    
def show_contacts(phone_list: list):
    if len(phone_list) < 1:
        print('Телефонная книга пуста или не открыта')
    else:
        print()
        for i, contact in enumerate(phone_list, 1):
            print(f'\t{i}. {contact[0]:20} {contact[1]:13} {contact[2]:20}')
        print()

def input_error():
    print('Ошибка ввода. Введите корректный пункт меню')

def empty_request():
    print('Искомый контакт не найден!')

def many_request():
    print('Введите более точные данные. Найдено более одного контакта! ')

def end_program():
    print('Программа завершена')

def create_new_contact():
    name = input('Введите имя и фамилию: ')
    phone = input('Введите телефон ')
    comment = input('Введите комментарий ')
    return name, phone, comment

def find_contact():
    find = input('Введите искомый элемент: ')
    return find

def select_contact(message: str):
    contact = input(message)
    return contact

def change_contact():
    print('Введите новые данные (если изменения не требуются нажмите Enter')
    name = input('Введите имя и фамилию: ')
    phone = input('Введите телефон ')
    comment = input('Введите комментарий ')
    return name, phone, comment

def delete_confirm(contact: str):# Он будет принимать контакт это будет строка
    result = input(f'Вы действительно хотите удалить контакт {contact}? (y/n)').lower()####### Переводим в lower кейс если будут большие буквы, то автоматом переведутся в маленькие
    if result == 'y':
        return True
    else:
        return False

def information(message):
    print(message)
