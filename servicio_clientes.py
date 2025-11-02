import servicio_concesionarias

class ServicioClientes:
    def obtener_total_ventas_por_cliente(self, concesionaria_id, cliente_id):
        servicio = servicio_concesionarias.ServicioConcesionarias()

        concesionaria = servicio.obtener_por_id(concesionaria_id)

        if concesionaria is None:
            return 0
        total = 0

        for sucursal in concesionaria.obtener_sucursales():
            for venta in sucursal.obtener_ventas():
                if venta.obtener_cliente_id() == int(cliente_id):
                    total += venta.obtener_monto()

        return total