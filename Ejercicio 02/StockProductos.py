from ProductoStock import ProductoStock

class StockProductos:
    def __init__(self):
        self.productos = {}

    def adiciona_producto(self, producto):
        self.productos[producto.nombre] = producto

    def obtener_producto(self, nombre):
        return self.productos.get(nombre, None)