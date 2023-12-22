import json
import easygui as eg


fields = ["Имя пользователя", "Номер телефона"]

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
    msg = "Выберите команду"
    title = "Телефонный справочник"
    choices = ["/save", "/all", "/add", "/exit"]

    command = eg.choicebox(msg, title, choices)
    if (command == "/exit"):
        break
    elif command == "/save":
        save()
    elif command == "/all":
        eg.msgbox(phonebook)
    elif command == "/add":
        contact = eg.multenterbox("Введите данные", title, fields)
        name = contact[0]
        phone = contact[1].split()
        if phone != "":
            phonebook[name] = phone
        elif name != "":
            phonebook[name] = name
        else:
            continue
    else:
        eg.msgbox("Вы ввели неверную команду!")