import Contacto
class Agenda:
    def __init__(self):
        self.contactos = []

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if nombre.lower() in contacto.nombre.lower():
                return contacto
        return None
    
    def insertar_modificar_contacto(self, contacto):
        encontrado = False
        for i, c in enumerate(self.contactos):
            if c.nombre == contacto.nombre:
                self.contactos[i] = contacto
                encontrado = True
                break
        if not encontrado:
            self.contactos.append(contacto)

    def eliminar_contacto(self, nombre):
        for i, contacto in enumerate(self.contactos):
            if contacto.nombre == nombre:
                del self.contactos[i]
                break

    def listar_contactos(self):
        for i, contacto in enumerate(self.contactos, start=1):
            print(f"Contacto {i}:")
            print(contacto)

    def guardar_agenda(self, archivo):
        with open(archivo, 'w') as f:
            for contacto in self.contactos:
                f.write(f"{contacto.nombre},{contacto.telefono},{contacto.direccion},{contacto.relacion}\n")
    
    def cargar_agenda(self, archivo):
        with open(archivo, 'r') as f:
            for linea in f:
                nombre, telefono, direccion, relacion = linea.strip().split(',')
                self.insertar_modificar_contacto(Contacto(nombre, telefono, direccion, relacion))
    