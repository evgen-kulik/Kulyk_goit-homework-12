from collections import UserDict
from datetime import datetime
import json


class AddressBook(UserDict):
    """Містить логіку пошуку в телефонній книзі"""

    def __init__(self):
        self.data = {}
        self.current_index = 0

    def add_record(self, record):
        """Додає дані у self.data"""
        self.data[record.name] = record.data
        return self.data

    def find(self, name):
        """Виконує пошук телефону по імені"""
        return self.data[name]

    def __iter__(self):
        return self

    def __next__(self):
        # Перетворимо словник з контактами в список для використання зрізу
        lst_dct = []
        for name, record in self.data.items():
            lst_dct.append(name)
            lst_dct.append(record)
        if self.current_index < len(lst_dct):
            lst_dct_para = lst_dct[self.current_index: self.current_index+4]
            self.current_index += 4
            return 'Пара контактів:\n' + str(lst_dct_para)
        raise StopIteration

    def show_all_contacts(self):
        """Виводить на екран всю книгу"""
        print(f'Всі контакти:\n{self.data}')

    def write_contacts_to_file(self):
        """Зберігає адресну книгу у файл на диск"""
        with open('data.json', 'w') as fh:
            json.dump(self.data, fh)

    def read_contacts_from_file(self):
        """Завантажує адресну книгу з файлу на диску"""
        with open('data.json', 'r') as fh:
            self.data = json.load(fh)
            print(self.data)
            return self.data


class Record:
    """
    Відповідає за логіку додавання/видалення/редагування необов'язкових
    полів та зберігання обов'язкового поля name
    """

    def __init__(self, name, data):
        self.name = name
        self.data = data

    def update(self, data):
        """Оновлює self.data"""
        self.data = data
        return self.data

    def days_to_birthday(self, next_day_of_birth):
        """Повертає кількість днів до дня народження"""
        if len(next_day_of_birth) == 10:
            current_datetime = datetime.now()
            lst_date = next_day_of_birth.split('-')
            lst_date = list(map(int, lst_date))
            date_dt = datetime(year=lst_date[0], month=lst_date[1], day=lst_date[2])
            difference = date_dt - current_datetime
            print(f'До дня народження - {difference.days} днів')
            return difference.days



class Name:
    """Містить обов'язкове поле з ім'ям"""

    def __init__(self, name):
        self.name = name

    # Наступні два методи виконують перевірку коректності імені
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name and isinstance(name, str):
            self.__name = name
        else:
            print("Ім'я введено некоректно!")


class Phone:
    """Містить необов'язкове поле з телефоном"""

    def __init__(self, lst_phones):
        self.lst_phones = lst_phones

    # Наступні два методи виконують перевірку наявності телефонів
    @property
    def lst_phones(self):
        return self.__lst_phones

    @lst_phones.setter
    def lst_phones(self, lst_phones):
        if lst_phones:
            self.__lst_phones = lst_phones
        else:
            print("Телефоний список порожній!")


class Birthday:
    """Містить дату найближчого дня народження"""
    next_day_of_birth = ''  # 'рік-місяць-день'


# Створимо та занесемо 1-го користувача до поля data
user_1_name = Name('Garry')
user_1_phones = Phone(['+111', '+222'])
user_1_birth = Birthday()
user_1_birth.next_day_of_birth = '2023-12-31'
changing = Record(user_1_name.name, user_1_phones.lst_phones)
address_book = AddressBook()
address_book.add_record(changing)

# Кількість днів до найближчого дня народження користувача
changing.days_to_birthday(user_1_birth.next_day_of_birth)

# Створимо та занесемо 2-го користувача до поля data
user_2_name = Name('Tom')
user_2_phones = Phone(['+333', '+444'])
changing = Record(user_2_name.name, user_2_phones.lst_phones)
address_book.add_record(changing)

# Змінемо номери телефонів у user_2
changing.update(['+330', '+440'])
address_book.add_record(changing)

# Виконаємо пошук по адресній книзі
print('Результат пошуку: ', end='')
print(address_book.find('Tom'))
print('Результат пошуку: ', end='')
print(address_book.find('Garry'))

# Створимо та занесемо 3-го користувача до поля data
user_3_name = Name('Babba')
user_3_phones = Phone(['+555', '+566'])
changing = Record(user_3_name.name, user_3_phones.lst_phones)
address_book.add_record(changing)
# Створимо та занесемо 4-го користувача до поля data
user_4_name = Name('Merry')
user_4_phones = Phone(['+777', '+888'])
changing = Record(user_4_name.name, user_4_phones.lst_phones)
address_book.add_record(changing)

# Виведемо по два контакти з адресної книги
for i in address_book:
    print(i)

# Виведемо на екран всю адресну книгу у вигляді словника
address_book.show_all_contacts()

# Збережемо адресну книгу у файл 'data.json'
address_book.write_contacts_to_file()

# Завантажимо адресну книгу з файлу 'data.json'
print("Завантажимо адресну книгу з файлу 'data.json'")
address_book.read_contacts_from_file()

