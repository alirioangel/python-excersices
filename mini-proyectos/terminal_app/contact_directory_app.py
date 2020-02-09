from contact_book import ContactBook


def run():
    contact_book = ContactBook()
    try:
        contact_book.load()
    except:
        print('No existen contactos actualmente!. agregue al primero')

    while True:
        command = input('''
        ¿Qué desea hacer?

        [a]gregar contacto
        [ac]tualizar contacto
        [b]uscar contacto
        [l]istar contactos
        [e]liminar contacto
        [s]alir
        ''')

        if command == 'a':
            name = input('Escribe el nombre del contacto:\n')
            phone_number = input('Escribe el telefono del contacto:\n')
            email = input('Escribe el email del contacto:\n')
            contact_book.add(name, phone_number, email)
            print('Contacto Añadido')
        elif command == 'ac':
            name = input('Escribe el nombre del contacto:\n')
            while True:
                ac_command = input('''
                ¿Qué deseas modificar?

                [n]ombre
                [te]lefono
                [c]orreo electronico
                [t]odo
                [ca]ncelar
                ''')
                if ac_command == 'n':
                    new_name = input('Escribe el nuevo nombre:\n')
                    contact_book.update(name, new_name=new_name)
                    break
                elif ac_command == 'te':

                    new_phone_number = input('Escribe el nuevo telefono:\n')
                    contact_book.update(
                        name, new_phone_number=new_phone_number)
                    break
                elif ac_command == 'c':
                    new_email = input('Escribe el nuevo correo electronico:\n')
                    contact_book.update(name, new_email=new_email)
                    break
                elif ac_command == 't':
                    new_name = input('Escribe el nuevo nombre:\n')
                    new_phone_number = input('Escribe el nuevo telefono:\n')
                    new_email = input('Escribe el nuevo correo electronico:\n')
                    contact_book.update(
                        name, new_name=new_name, new_phone_number=new_phone_number, new_email=new_email)
                    break
                elif ac_command == 'ca':
                    print('Volviendo al menu principal')
                    break
                else:
                    print('Opcion invalida')
        elif command == 'b':
            name = input('Escribe el nombre del contacto:\n')
            contact_book.search(name)
        elif command == 'l':
            contact_book.show_all()
        elif command == 'e':
            name = input('Escribe el nombre del contacto a eliminar:\n')
            contact_book.delete_contact(name)
            print('Contacto eliminado satisfactoriamente')
        elif command == 's':
            print('Hasta pronto...')
            break
        else:
            print('Opcion invalida.')


if __name__ == '__main__':
    print('B I E N V E N I D O  A  T U  A G E N D A')
    print('Hecho por: Alirio Angel')
    run()
