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
    def agregar_contacto(self, contacto):
        existente = self.buscar_contacto(contacto.nombre)
        if existente:
            self.modificar_contacto(contacto.nombre, contacto)
        else:
            if self.ultima_posicion + 1 < self.max_contactos:
                self.contactos.append(contacto)
                self.ultima_posicion += 1
                print(f"Contacto agregado: {contacto}")
            else:
                print("La agenda está llena. No se puede agregar más contactos.")
    def eliminar_contacto(self, nombre):
        for i, contacto in enumerate(self.contactos):
            if contacto.nombre == nombre:
                del self.contactos[i]
                return
        print("Contacto no encontrado.")  
    def modificar_contacto(self, nombre, nuevo_nombre=None, nuevo_numero_telefono=None, nueva_direccion=None, nueva_relacion=None):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                if nuevo_nombre:
                    contacto.nombre = nuevo_nombre
                if nuevo_numero_telefono:
                    contacto.numero_telefono = nuevo_numero_telefono
                if nueva_direccion:
                    contacto.direccion = nueva_direccion
                if nueva_relacion:
                    contacto.relacion = nueva_relacion
                print(f"Contacto '{nombre}' modificado exitosamente.")
                return
        print("Contacto no encontrado.")
    def listar_contactos(self):
        for contacto in self.contactos:
            print(contacto)
