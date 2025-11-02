import vehiculo


class Moto(vehiculo.Vehiculo):

    def __init__(
        self, numero_id, marca, modelo, anio, sucursal_id, estado_id, cilindrada
    ):
        super().__init__(numero_id, marca, modelo, anio, sucursal_id, estado_id)
        self.__cilindrada = cilindrada

    def establecer_cilindrada(self, cilindrada):
        self.__cilindrada = cilindrada

    def obtener_cilindrada(self):
        return self.__cilindrada
<<<<<<< HEAD
    
    
    def __str__(self):
        return (f"Moto(id={self.obtener_numero_id()}, marca='{self.obtener_marca()}', "
                f"modelo='{self.obtener_modelo()}', anio={self.obtener_anio()}, "
                f"sucursal_id={self.obtener_sucursal_id()}, estado_id={self.obtener_estado_id()}, "
                f"cilindrada={self.__cilindrada})")
=======
>>>>>>> origin/main
