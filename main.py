import json


phonebook = {"Дядя Ваня": {'phones': [8311654654, 89654515],
                           'birthday': "05.05.1990", 'email': "12@ya.ru"},
             "Дядя Вася": {'phones': [54654541]}
             }


def load():
    with open("phoneNumber", "r", encoding="utf-8") as fh:
        phonebook = json.load(fh)
    print("Наш контакт был успешно загружен из файла phoneNumber.json")


def save():
    with open("phoneNumber.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(phonebook, ensure_ascii=False))
    print("Наш контакт был успешно сохранен в файле phoneNumber.json")

# print(phonebook['Дядя Ваня'])
# print(phonebook['Дядя Ваня']['phones'])
# print(phonebook['Дядя Ваня']['phones'][0])

for name, values in phonebook.items():
    print(name, values)
print("Открыт телефонный справочник")

try:
    load()
except:
    phonebook = {"Дядя Ваня": {'phones': [8311654654, 89654515],
                               'birthday': "05.05.1990", 'email': "12@ya.ru"},
                 "Дядя Вася": {'phones': [54654541]}
                 }

while True:
    command = input("Введите команду ")
    if (command == "/exit"):
        break
    elif command == "/save":
        save()
    elif command == "/all":
        print("Текущий телефонный список: ")
        print(phonebook)
    elif command == "/add":
        name = input("Введите имя пользователя: ")
        phone = input("Введите номера телефонов через пробел: ").split()
        if phone != "":
            phonebook[name] = phone
        elif name != "":
            phonebook[name] = name
        else:
            continue
    else:
        print("Вы ввели не верную комманду!")