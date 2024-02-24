from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if len(value) !=0:   # перевірка чи ім'я не порожнє
            super().__init__(value)
        else:
            raise ValueError ("Enter your name")
        
	  
class Phone(Field):
      def __init__(self, value):
        if len(value) == 10: #перевірка  формату номера
            super().__init__(value)
        else:
            raise ValueError("Enter a valid phone number")
	

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
#Додавання номера телефону
    def add_phone(self, phone):
        self.phones.append(Phone(phone))
#Видалення номера телефону          
    def remove_phone(self, phone):  
        for phone in self.phones:
            if phone.value == phone:
                self.phones.remove(phone)
#Редагування номера телефону     
    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                print(f"Contact phone numbe {old_phone} edited on {new_phone} ")
        
#Знаходження номера телефону     
    def find_phone(self, phone):
        return [p for p in self.phones if p.value == phone]



    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record): # Додавання запису 
        self.data[record.name.value] = record

    def find(self, name):  # Пошук запису за ім'ям
        return self.data.get(name)

    def delete(self, name):  # Видалення запису за іменем
        if name in self.data:
            del self.data[name]  

if __name__ == "__main__":
     
# Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")


   


        

