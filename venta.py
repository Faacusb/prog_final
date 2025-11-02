class Venta:
    def __init__(self, numero_id, fecha, cliente_id, vehiculo_id, monto):
        self.__numero_id = numero_id
        self.__fecha = fecha
        self.__cliente_id = cliente_id
        self.__vehiculo_id = vehiculo_id
        self.__monto = monto

    def establecer_numero_id(self, numero_id):
        self.__numero_id = numero_id

    def establecer_fecha(self, fecha):
        self.__fecha = fecha

    def establecer_cliente_id(self, cliente_id):
        self.__cliente_id = cliente_id

    def establecer_vehiculo_id(self, vehiculo_id):
        self.__vehiculo_id = vehiculo_id

    def establecer_monto(self, monto):
        self.__monto = monto



    def obtener_numero_id(self):
        return self.__numero_id

    def obtener_fecha(self):
        return self.__fecha

    def obtener_cliente_id(self):
        return self.__cliente_id

    def obtener_vehiculo_id(self):
        return self.__vehiculo_id

    def obtener_monto(self):
        return self.__monto
    
    

    def __eq__(self, other):
        return isinstance(other, Venta) and self.__numero_id == other.__numero_id

    def __str__(self):
        return (f"Venta(id={self.__numero_id}, fecha='{self.__fecha}', "
                f"cliente_id={self.__cliente_id}, vehiculo_id={self.__vehiculo_id}, "
                f"monto={self.__monto})")