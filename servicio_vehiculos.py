#Ejercicio 7
import servicio_concesionarias

class ServicioVehiculos:
    def __init__(self):
        self.__servicio_concesionarias = servicio_concesionarias.ServicioConcesionarias()

    def obtenerVehiculosPorSucursalYEstado(self, concesionariaID, sucursalID, estadoID):
        concesionaria = self.__servicio_concesionarias.obtenerPorId(concesionariaID)
        if concesionaria is None or not hasattr(concesionaria, "obtener_sucursales"):
            return []

        sucursal_obj = None
        for sucursal in concesionaria.obtener_sucursales():
            if hasattr(sucursal, "obtener_numero_id") and sucursal.obtener_numero_id() == sucursalID:
                sucursal_obj = sucursal
                break

        if sucursal_obj is None or not hasattr(sucursal_obj, "obtener_vehiculos"):
            return []

        vehiculos_filtrados = []
        for vehiculo in sucursal_obj.obtener_vehiculos():
            if hasattr(vehiculo, "obtener_estado_id") and vehiculo.obtener_estado_id() == estadoID:
                vehiculos_filtrados.append(vehiculo)

        return vehiculos_filtrados
