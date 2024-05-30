class Contacto:
    def __init__(self, nombre, telefono, direccion, relacion ):
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.relacion = relacion
    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Dirección: {self.direccion}, Relación: {self.relacion}"