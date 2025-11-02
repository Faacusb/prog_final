class Cliente:
<<<<<<< HEAD
    def __init__(self, numero_id, nombre, apellidos, email):
        self.__numero_id = numero_id
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__email = email



    def establecer_numero_id(self, numero_id):
        self.__numero_id = numero_id

    def establecer_nombres(self, nombre):
        self.__nombre = nombre

    def establecer_apellidos(self, apellidos):
        self.__apellidos = apellidos

    def establecer_email(self, email):
        self.__email = email



    def obtener_numero_id(self):
        return self.__numero_id

    def obtener_nombres(self):
        return self.__nombre

    def obtener_apellidos(self):
        return self.__apellidos

    def obtener_email(self):
        return self.__email


    def __eq__(self, other):
        return isinstance(other, Cliente) and self.__numero_id == other.__numero_id

    def __str__(self):
        return (f"Cliente(id={self.__numero_id}, nombre='{self.__nombre}', "
                f"apellidos='{self.__apellidos}', email='{self.__email}')")
=======
    def __init__(self, numeroId, nombre, apellidos, mail):
        self.__numeroId = numeroId
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__email = mail

    def establecerNumeroId(self, numero_id):
        self.__numero_id = numero_id

    def establecerNombres(self, nombres):
        self.__nombre = nombres

    def establecerApellidos(self, apellidos):
        self.__apellidos = apellidos

    def establecerEmail(self, email):
        self.__email = email

    def obtenerNumeroId(self):
        return self.__numero_id
    
    def obtenerNombres(self):
        return self.__nombre
    
    def obtenerApellidos(self):
        return self.__apellidos
    
    def obtenerEmail(self):
        return self.__email
>>>>>>> origin/main
