#Ejercicio 7
import servicio_concesionarias

class ServicioVehiculos:
    def obtener_vehiculos_por_sucursal_y_estado(self, concesionaria_id, sucursal_id, estado_id):
        servicio_concesionarias_obj = servicio_concesionarias.ServicioConcesionarias()
        concesionaria = servicio_concesionarias_obj.obtener_por_id(concesionaria_id)
        if concesionaria is None:
            return []

        concesionaria_id = int(concesionaria_id)
        sucursal_id = int(sucursal_id)
        estado_id = int(estado_id)

        vehiculos_filtrados = []

        for vehiculo in concesionaria.obtener_vehiculos():
            if vehiculo.obtener_sucursal_id() == sucursal_id and vehiculo.obtener_estado_id() == estado_id:
                vehiculos_filtrados.append(vehiculo)

        return vehiculos_filtrados
