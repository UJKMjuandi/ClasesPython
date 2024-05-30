from ProductoStock import ProductoStock
from StockProductos import StockProductos
from CarritoCompra import CarritoCompra

def main():
    stock = StockProductos()
    stock.adiciona_producto(ProductoStock("monitor", 500, 100))
    stock.adiciona_producto(ProductoStock("teléfono", 150, 300))
    stock.adiciona_producto(ProductoStock("teclado", 70, 50))
    stock.adiciona_producto(ProductoStock("mouse", 50, 50))

    carrito = CarritoCompra(stock)
    carrito.adiciona_item("monitor", 2)
    carrito.adiciona_item("teléfono", 5)
    carrito.adiciona_item("teclado", 2)
    carrito.finalizar_compra()

    print("La suma de los productos: ", carrito.calcula_total())


main()

