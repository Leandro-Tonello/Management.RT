class repuesto:
    def __init__(self, id, marca, tipo, modelo, descripcion, color, stock_minimo, aplicable, stock, precio):
       selfid = id
       self.marca = marca
       self.tipo = tipo
       self.modelo = modelo
       self.descripcion = descripcion
       self.color = color
       self.stock_minimo = stock_minimo
       self.stock = stock
       self.aplicable = aplicable
       self.precio = precio.

    def descontar_stock(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            print(f"Se han descontado {cantidad} unidades del stock de {self.descripcion}.")
        else:
            print("No hay suficiente stock disponible.")

    def agregar_stock(self, cantidad):
        self.stock += cantidad
        

