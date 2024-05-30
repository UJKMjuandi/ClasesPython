from StockProductos import StockProductos

class CarritoCompra:
    def __init__(self, stock):
        self.stock = stock
        self.items = {}

    def adiciona_item(self, nombre, cantidad):
        producto = self.stock.obtener_producto(nombre)
        if producto and producto.cantidad >= cantidad:
            if nombre in self.items:
                self.items[nombre] += cantidad
            else:
                self.items[nombre] = cantidad
            producto.cantidad -= cantidad
        else:
            print(f"No hay suficiente stock de {nombre} o el producto no existe.")

    def finalizar_compra(self):
        for nombre, cantidad in self.items.items():
            print(f"{nombre}: {cantidad} unidades")

    def calcula_total(self):
        total = 0
        for nombre, cantidad in self.items.items():
            producto = self.stock.obtener_producto(nombre)
            if producto:
                total += producto.precio * cantidad
        return total