import csv
from contact import Contact


class ContactBook:

    def __init__(self):
        self._contacts = []

    def add(self, name, phone_number, email):
        contact = Contact(name, phone_number, email)
        self._contacts.append(contact)
        self._save()

    def update(self, name, *args, **kwargs):
        new_name = kwargs.get('new_name', None)
        new_phone_number = kwargs.get('new_phone_number', None)
        new_email = kwargs.get('new_email', None)

        for contact in self._contacts:
            if contact._name.lower() == name.lower():
                contact._name = new_name.capitalize() if new_name != None else name.capitalize()
                contact._phone_number = new_phone_number if new_phone_number != None else contact._phone_number
                contact._email = new_email if new_email != None else contact._email
                self._save()
                break
        else:
            self._not_found()

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def search(self, name):
        for contact in self._contacts:
            if contact._name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found()

    def delete_contact(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact._name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                break

    def _print_contact(self, contact):
        print('*-------*--------*-------*--------*-------*--------*')
        print('Nombre: {}'.format(contact._name))
        print('Telefono: {}'.format(contact._phone_number))
        print('Correo Electronico: {}'.format(contact._email))
        print('*-------*--------*-------*--------*-------*--------*')

    def _not_found(self):
        print('*-------*--------*-------*--------*-------*--------*')
        print('No se encontro contacto con ese nombre')
        print('*-------*--------*-------*--------*-------*--------*')

    def _save(self):
        with open('contactos.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(('name', 'phone_number', 'email'))
            for contact in self._contacts:
                writer.writerow(
                    (contact._name, contact._phone_number, contact._email))

    def load(self):
        with open('contactos.csv', 'r') as f:
            reader = csv.reader(f)
            for idx, contact in enumerate(reader):
                if idx == 0:
                    continue
                self.add(contact[0], contact[1], contact[2])
