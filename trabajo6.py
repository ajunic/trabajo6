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
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.fecha_nacimiento = fecha_nacimiento
    
    def crear_persona(self):
        return Persona(self.nombre, self.apellido, self.cedula, self.direccion, self.telefono, self.email, self.fecha_nacimiento)



class Estudiante(Persona):
    def __init__(self, id_estudiante):
        self.id_estudiante = id_estudiante

class Profesor(Persona):
    def __init__(self, id_profesor):
        self.id_profesor = id_profesor


       


    

