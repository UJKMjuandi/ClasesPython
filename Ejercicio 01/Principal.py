from Contacto import Contacto
from Agenda import Agenda

class Principal:
    def __init__(self):
        self.agenda = Agenda()

    def menu(self):
        while True:
            print("\n1. Agregar contacto")
            print("2. Buscar contacto")
            print("3. Eliminar contacto")
            print("4. Modificar contacto")
            print("5. Listar contactos")
            print("6. Salir")
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                nombre = input("Ingrese el nombre del contacto: ")
                numero_telefono = input("Ingrese el número de teléfono: ")
                direccion = input("Ingrese la dirección: ")
                relacion = input("Ingrese la relación: ")
                self.agenda.agregar_contacto(Contacto(nombre, numero_telefono, direccion, relacion))
            elif opcion == 2:
                nombre = input("Ingrese el nombre del contacto a buscar: ")
                contacto = self.agenda.buscar_contacto(nombre)
                if contacto:
                    print(contacto)
                else:
                    print("Contacto no encontrado.")
            elif opcion == 3:
                nombre = input("Ingrese el nombre del contacto a eliminar: ")
                self.agenda.eliminar_contacto(nombre)
            elif opcion == 4:
                nombre = input("Ingrese el nombre del contacto a modificar: ")
                nuevo_nombre = input("Nuevo nombre (opcional): ")
                nuevo_numero_telefono = input("Nuevo número de teléfono (opcional): ")
                nueva_direccion = input("Nueva dirección (opcional): ")
                nueva_relacion = input("Nueva relación (opcional): ")
                self.agenda.modificar_contacto(nombre, nuevo_nombre=nuevo_nombre, nuevo_numero_telefono=nuevo_numero_telefono, nueva_direccion=nueva_direccion, nueva_relacion=nueva_relacion)
            elif opcion == 5:
                self.agenda.listar_contactos()
            elif opcion == 6:
                break
            else:
                print("Opción inválida. Inténtelo de nuevo.")

if __name__ == "__main__":
    principal = Principal()
    principal.menu()
