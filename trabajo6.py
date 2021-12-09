"""La Universidad de Oxford ubicada en inglaterra lo ha contratado a usted para que 
desarrolle un sistema de control academico estudiantil, para tal tarea se cuenta con la 
siguiente información"""

#Author: Armando Jose Ugarte
#Rodolfo Melendez
#Michael Gomez.

"""Programar la siguiente jerarquia de clases, con su correspondiente prueba de ejecución
en base a lo aprendido en las sesiones de Object-oriented programming – OOP (Esto es 
Class Factory y el uso del decorador @property para la implementación y/o 
operacionalización de propiedades)."""

class Persona:
    def __init__(self, nombre, apellido, cedula, direccion, telefono, email,fecha_nacimiento):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cedula = cedula
        self.__direccion = direccion
        self.__telefono = telefono
        self.__email = email
        self.__fecha_nacimiento = fecha_nacimiento
    
    def crear_persona(self):
        return Persona(self.nombre, self.apellido, self.cedula, self.direccion, self.telefono, self.email, self.fecha_nacimiento)

    # define setter and getter methods for Persona attributes
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def set_apellido(self, apellido):
        self.__apellido = apellido

    def get_cedula(self):
        return self.__cedula
    
    def set_cedula(self, cedula):
        self.__cedula = cedula
    
    def get_direccion(self):
        return self.__direccion
    
    def set_direccion(self, direccion):
        self.__direccion = direccion
    
    def get_telefono(self):
        return self.__telefono
    
    def set_telefono(self, telefono):
        self.__telefono = telefono

    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        self.__email = email

    def get_fecha_nacimiento(self):
        return self.__fecha_nacimiento
    
    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.__fecha_nacimiento = fecha_nacimiento

    # Property definitions for each attribute.
    nombre = property(get_nombre, set_nombre)
    apellido = property(get_apellido, set_apellido)
    cedula = property(get_cedula, set_cedula)
    direccion = property(get_direccion, set_direccion)
    telefono = property(get_telefono, set_telefono)
    email = property(get_email, set_email)
    fecha_nacimiento = property(get_fecha_nacimiento, set_fecha_nacimiento)

class Estudiante(Persona):
    def __init__(self, id_estudiante):
        self.__id_estudiante = id_estudiante

    # define setter and getter methods for Estudiante attributes
    def get_id_estudiante(self):
        return self.__id_estudiante

    def set_id_estudiante(self, id_estudiante):
        self.__id_estudiante = id_estudiante

class Profesor(Persona):
    def __init__(self, id_profesor):
        self.__id_profesor = id_profesor

    # define setter and getter methods for Profesor attributes
    def get_id_profesor(self):
        return self.__id_profesor

    def set_id_profesor(self, id_profesor):
        self.__id_profesor = id_profesor




class Analytics:
    def __init__(self, media, moda,mediana, minimo,maximo):
        self.__media = media
        self.__moda = moda
        self.__mediana = mediana
        self.__minimo = minimo
        self.__maximo = maximo
    
    #define setter and getter methods for Analytics attributes
    def get_media(self):
        return self.__media
    def set_media(self, media):
        self.__media = media

    def get_moda(self):
        return self.__moda
    def set_moda(self, moda):
        self.__moda = moda
    
    def get_mediana(self):
        return self.__mediana
    def set_mediana(self, mediana):
        self.__mediana = mediana
    
    def get_minimo(self):
        return self.__minimo
    def set_minimo(self, minimo):
        self.__minimo = minimo

    def get_maximo(self):
        return self.__maximo
    def set_maximo(self, maximo):
        self.__maximo = maximo

    # Property definitions for each attribute.
    media = property(get_media, set_media)
    moda = property(get_moda, set_moda)
    mediana = property(get_mediana, set_mediana)
    minimo = property(get_minimo, set_minimo)
    maximo = property(get_maximo, set_maximo)
    






    pass    


       


    

