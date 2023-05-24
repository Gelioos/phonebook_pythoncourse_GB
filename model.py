import json

data = {}

def addContact(data):
    contact_id = max(data.keys()) + 1 if len(data) > 0 else 1
    name = input('Введите ФИО: ')
    phone = input('Введите номер телефона: ')
    data[contact_id] = {'name': name, 'phone': phone} 

def saveContact(data):
    with open("data_file.json", "w", encoding='utf-8') as write_file:
        write_file.write(json.dumps(data)) # сбрасывает данные в файл

def readContact(data):
    with open("data_file.json", "r", encoding='utf-8') as read_file:
        temp = json.loads(read_file.read())
    for key, value in temp.items():
        data[int(key)] = value
    return data

def changeContact(data):
    print(data)
    x = int(input('Какой id контакта поменять? '))
    print(data[x])
    name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    if len(name) > 0:
        data[x]['name'] = name
    if len(phone) > 0:
        data[x]['phone'] = phone

def findContact(data):
    command = int(input('Меню: \n1. Искать по id \n2. Искать по имени \n3. Искать по телефону \n:'))
    match command:
        case 1: 
            print(data[int(input('Введите id: '))])
        case 2:
            fn = input('Введите имя: ').lower()
            for key, values in data.items():
                if values['name'].lower().find(fn) != -1:
                    print(key, values)
        case 3:
            fn = input('Введите номер телефона: ')
            for key, values in data.items():
                if values['phone'].find(fn) != -1:
                    print(key, values)            
                    
#def deleteContact():
    

def menuContacts(menu):
    for key, item in menu.items():
        print(key, item)