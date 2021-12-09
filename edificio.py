class Edificio:
    def __init__(self, nombre_edificio, direccion, cantidad_pisos, cantidad_aulas):
        self.__nombre_edificio = nombre_edificio
        self.__direccion = direccion
        self.__cantidad_pisos = cantidad_pisos
        self.__cantidad_aulas = cantidad_aulas

    #Defining Getters and Setters
    def get_nombre_edificio(self):
        return self.__nombre_edificio
    def set_nombre_edificio(self, nombre_edificio):
        self.__nombre_edificio == nombre_edificio
    def get_direccion(self):
        return self.__direccion
    def set_direccion(self, direccion):
        self.__direccion == direccion
    def get_cantidad_pisos(self):
        return self.__cantidad_pisos
    def set_cantidad_pisos(self, cantidad_pisos):
        self.__cantidad_pisos == cantidad_pisos
    def get_cantidad_aulas(self):
        return self.__cantidad_pisos
    def set_cantidad_aulas(self, cantidad_aulas):
        self.__cantidad_aulas == cantidad_aulas

    #Property definitions for each attribute.

    nombre_edifcio = property(get_nombre_edificio, set_nombre_edificio)
    direccion = property(get_direccion,set_direccion)
    cantidad_pisos = property(get_cantidad_pisos, set_cantidad_pisos)
    cantidad_aulas = property(get_cantidad_aulas, get_cantidad_aulas)


    def administrar_Edificio(): #Devolvera None
        pass
