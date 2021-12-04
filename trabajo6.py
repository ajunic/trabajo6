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

class Tipo_profesor:
    def __init__(self, tipo_profesor):
        self.tipo_profesor = tipo_profesor

class Turno:
    def __init__(self, turno):
        self.turno = turno

class Matricula:
    def __init__(self, fecha_matricula, hora_matricula):
        self.fecha_matricula = fecha_matricula
        self.hora_matricula = hora_matricula

class Curso:
    def __init__(self,  nombre_curso, creditos, horas_semanales, programa,nota):
        self.nota = nota #agregada para punto 7
        self.nombre_curso = nombre_curso
        self.creditos = creditos
        self.horas_semanales = horas_semanales
        self.programa = programa
class Edificio:
    def __init__(self, nombre_edificio, direccion, cantidad_pisos, cantidad_aulas):
        self.nombre_edificio = nombre_edificio
        self.direccion = direccion
        self.cantidad_pisos = cantidad_pisos
        self.cantidad_aulas = cantidad_aulas

class Aula:
    def __init__(self, nombre_aula, numero_piso, numero_edificio, capacidad_asientos):
        self.nombre_aula = nombre_aula
        self.numero_piso = numero_piso
        self.numero_edificio = numero_edificio
        self.capacidad_asientos = capacidad_asientos

class Programa:
    def __init__(self, nombre, fecha_creacion, status_programa, director):
        self.nombre = nombre
        self.fecha_creacion = fecha_creacion
        self.status_programa = status_programa
        self.director = director


class Analytics:
    pass    


       


    

