from Contacto import Contacto
from Agenda import Agenda

class Principal:
    def __init__(self):
        self.agenda = Agenda()

    def mostrar_menu(self):
        print("MENU:")
        print("1-Agregar contacto")
        print("2-Modificar contacto")
        print("3-Eliminar contacto")
        print("4-Listar contactos")
        print("5-Salir")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_contacto_manualmente()
            elif opcion == "2":
                self.modificar_contacto()
            elif opcion == "3":
                self.eliminar_contacto()
            elif opcion == "4":
                self.agenda.listar_contactos()
            elif opcion == "5":
                print("chau baboso UwU")
                break
            else:
                print("opcion no valida, ingrese otra opcion")

    def agregar_contacto_manualmente(self):
        nombre = input("Ingrese el nombre: ")
        telefono = input("Ingrese el número de teléfono: ")
        direccion = input("Ingrese la dirección: ")
        relacion = input("Ingrese la relación: ")
        nuevo_contacto = Contacto(nombre, telefono, direccion, relacion)
        self.agenda.insertar_modificar_contacto(nuevo_contacto)

    def modificar_contacto(self):
        nombre = input("Ingrese el nombre del contacto a modificar: ")
        contacto_existente = self.agenda.buscar_contacto(nombre)
        if contacto_existente:
            print("Contacto encontrado:")
            print(contacto_existente)
            nuevo_telefono = input("Ingrese el nuevo número de teléfono: ")
            nuevo_direccion = input("Ingrese la nueva dirección: ")
            nueva_relacion = input("Ingrese la nueva relación: ")
            if nuevo_telefono:
                contacto_existente.telefono = nuevo_telefono
            if nuevo_direccion:
                contacto_existente.direccion = nuevo_direccion
            if nueva_relacion:
                contacto_existente.relacion = nueva_relacion
            print("Contacto modificado exitosamente")
        else:
            print("No se encontró ningún contacto con ese nombre")

    def eliminar_contacto(self):
        nombre = input("Ingrese el nombre del contacto a eliminar: ")
        self.agenda.eliminar_contacto(nombre)
        print("Contacto eliminado exitosamente")

principal = Principal()
principal.ejecutar()