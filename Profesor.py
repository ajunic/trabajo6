from datetime import date

from Aula import Aula
from Curso import Curso
from Persona import Persona
from Programa import Programa


class Profesor(Persona):
    contador_profesor = 0
    listaProfesor = []

    def __init__(self, tipo, nombre, apellido, cedula, direccion, telefono, fecha_nacimiento,
                 email, codigo_profesor, obj_programa, obj_curso):#none
        Profesor.contador_profesor = + 1
        super().__init__(tipo, nombre, apellido, cedula, direccion, telefono, fecha_nacimiento, email)
        self.__id_profesor = Profesor.contador_profesor
        self.codigo_profesor = codigo_profesor
        self.obj_programa = obj_programa
        self.obj_curso = obj_curso

    def __str__(self):
        return f"""\nProfesor:[ ID: {self.__id_profesor}
        #Carnet: {self.codigo_profesor}
        #Programa: {self.obj_programa}
        #Curso: {self.obj_curso}]
        {super().__str__()}
        """
    # define setter and getter methods for Estudiante attributes
    def get_codigo_profesor(self):
        return self.__codigo_profesor

    def set_codigo_profesor(self, codigo_profesor):
        self.__codigo_profesor = codigo_profesor
    #Property
    codigo_profesor = property(get_codigo_profesor, set_codigo_profesor)
