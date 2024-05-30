import Contacto
class Agenda:
    def __init__(self):
        self.contactos = []
        self.max_contacts = 1000
        self.ultimo = -1

    def buscar_contacto(self, buscar):
        for contacto in self.contactos:
            if contacto.nombre == buscar:
                return contacto
        return None
    def insertar(self,contacto):
        if len(self.contactos) < self.max_contacts:
            self.contactos.append(contacto)
            self.ultimo += 1
            return True
        else:
            return False
    def eliminar(self,nombre):
        contacto = self.buscar_contacto(nombre)
        if contacto != None:
            self.contactos.remove(contacto)
            self.ultimo -= 1
            return True
        else:
            return False
    def modificar(self, nombre, nuevo_contacto):
        for i, contacto in enumerate(self.contactos):
            if contacto.nombre == nombre:
                self.contactos[i] = nuevo_contacto
                print(f"Contacto modificado: {nuevo_contacto}")
                return
        print("Contacto no encontrado.")
