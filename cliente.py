#Ejercicio 2
class Cliente:
    def __init__(self, numero_id, nombre, apellidos, email):
        self.__numero_id = numero_id
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__email = email

#Comandos
    def establecer_numero_id(self, numero_id):
        self.__numero_id = numero_id

    def establecer_nombres(self, nombre):
        self.__nombre = nombre

    def establecer_apellidos(self, apellidos):
        self.__apellidos = apellidos

    def establecer_email(self, email):
        self.__email = email

#Consultas
    def obtener_numero_id(self):
        return self.__numero_id

    def obtener_nombres(self):
        return self.__nombre

    def obtener_apellidos(self):
        return self.__apellidos

    def obtener_email(self):
        return self.__email

#Ejercicio 5
    def __eq__(self, other):
        return isinstance(other, Cliente) and self.__numero_id == other.__numero_id

    def __str__(self):
        return (f"Cliente(id={self.__numero_id}, nombre='{self.__nombre}', "
                f"apellidos='{self.__apellidos}', email='{self.__email}')")
