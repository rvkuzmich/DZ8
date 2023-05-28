"""Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения
и удаления данных"""

dict = {}
d = 1
with open('phonebook.txt', 'r', encoding='utf-8') as file:
    for i in file:
        i = i.replace('\n', '')
        dict[d] = list(i.split(';'))
        d += 1
def ShowEntry(dictionary):
    for i in dictionary:
        print (*dictionary[i])
def EntrySearch(dictionary):
    user_search = input('Введите поисковый запрос: ')
    for i in dictionary:
        for j in dictionary[i]:
            if user_search in j:
                print(*dictionary[i])
def AddEntry(dictionary):
    s = 1
    save = list(input('Введите фамилию, имя и телефон через пробел: ').split(' '))
    while True:
        if s in dictionary:
            s = s + 1
        else:
            dictionary[s] = save
            break
def DeleteEntry(dictionary):
    print(dictionary)
    s = int(input('Введите номер записи для удаления: '))
    if len(dictionary) < s:
            print('Такой записи не существует')
    else:    
        del dictionary[s]
def ChangeEntry(dictionary):
    print(dictionary)
    s = int(input('Укажите номер записи для изменения: '))
    if len(dictionary) < s:
            print('Такой записи не существует')
    else:
        k = int(input('Изменить: Фамилию(0) Имя(1) Телефон(2): '))    
        dictionary[s][k] = input('Введите новое значение: ')


menu = ['1 - Показать записи', '2 - Поиск по записям', '3 - Добавить запись', '4 - Изменить запись', '5 - Удалить запись', '6 - Выход']
save = ['Иванов', 'Иван', '89632212342']
save2 = ['Петров', 'Петр', '89653203947']

setpar = True
while setpar == True:
    print('Меню:')
    for i in menu:
        print(i)
    user_choice = int(input('Выберите действие: '))
    if user_choice < 1 or user_choice > 6:
        print('Такой опции нет')
    if user_choice == 1:
        ShowEntry(dict)
    elif user_choice == 2:
        EntrySearch(dict)
    elif user_choice == 3:
        AddEntry(dict)
    elif user_choice == 4:
        ChangeEntry(dict)
    elif user_choice == 5:
        DeleteEntry(dict)
    elif user_choice == 6:
        setpar = False
with open('phonebook.txt', 'w', encoding='utf-8') as file:
    for k in dict:
        file.write(f'{dict[k][0]};{dict[k][1]};{dict[k][2]}\n')
