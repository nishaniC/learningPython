import csv


class PhoneContact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class Phone:
    contacts = []
    def load_contacts_from_csv(self,filename):
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Phone.contacts.append(PhoneContact(row['Name'], row['Phone']))

    def search_contacts(self,search_phrase):
        found = False
        for contact in Phone.contacts:
            if (search_phrase.lower() in contact.name.lower()) or (search_phrase in contact.phone):
                print( contact.name," ",contact.phone)
                found = True
        if not found:
            print("No contacts found")

my_phone = Phone()
my_phone.load_contacts_from_csv('contacts.csv')
my_search_phrase = input("Search contacts: ")
my_phone.search_contacts(search_phrase=my_search_phrase)


