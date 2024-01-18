import random

class manzana:
    def __init__(self):
        self.manzanas = 3.5
        self.caramelos = 0.5

    def venta_de_manzana(self):
        self.venta_manzanas = random.randint(10,20)
        self.precio_manzanas = (self.venta_manzanas * self.manzanas)

    def venta_de_caramelos(self):
        self.venta_caramelos = random.randint(1,200)
        self.precio_caramelos = (self.venta_caramelos * self.caramelos)
        self.descuento = 0.7 * (self.venta_caramelos // 20)

    def tienda(self):
        print("Usted ha comprado",self.venta_manzanas,"manzanas y eso le ha costado",self.precio_manzanas,"€ ademas se ha comprado",self.venta_caramelos,"caramelos lo que le ha costado",self.precio_caramelos,"€ el total de su compra es",self.precio_manzanas+self.precio_caramelos,"€")
        if self.venta_caramelos >= 20:
            print("Se le ha aplicado un descuento de: ",self.descuento,"€")

tienda_manzanas = manzana()
tienda_manzanas.venta_de_manzana()
tienda_manzanas.venta_de_caramelos()
tienda_manzanas.tienda()


