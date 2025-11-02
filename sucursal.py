class Sucursal:
    def __init__(self, numero_id, direccion):
        self.__numero_id = numero_id
        self.__direccion = direccion
        self.__ventas = []


    def establecer_numero_id(self, numero_id):
        self.__numero_id = numero_id

    def establecer_direccion(self, direccion):
        self.__direccion = direccion

    def agregar_venta(self, venta):
        self.__ventas.append(venta)

    def remover_venta(self, venta):
        self.__ventas.remove(venta)

    def obtener_numero_id(self):
        return self.__numero_id

    def obtener_direccion(self):
        return self.__direccion

    def obtener_ventas(self):
        return self.__ventas

    def __eq__(self, other):
        return isinstance(other, Sucursal) and self.__numero_id == other.__numero_id

    def __str__(self):
        ventas_str = ", ".join(str(v) for v in self.__ventas) if self.__ventas else "sin ventas"
        return (f"Sucursal(id={self.__numero_id}, direccion='{self.__direccion}', "
                f"ventas=[{ventas_str}])")
