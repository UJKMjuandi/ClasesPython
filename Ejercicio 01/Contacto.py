class Contacto:
    def __init__(self, nombre, telefono, direccion, relacion ):
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.relacion = relacion
    
    def __str__(self):
        return f"Nombre: {self.nombre}\nTeléfono: {self.telefono}\nDirección: {self.direccion}\nRelación: {self.relacion}"