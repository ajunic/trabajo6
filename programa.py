from Curso import Curso


class Programa:
    contador_programas = 0

    def __init__(self,  nombre_programa, fecha_creacion_programa, status_programa, director, cursos):
        Programa.contador_programas +=1
        self.__id_programa = Programa.contador_programas
        self.__nombre_programa = nombre_programa
        self.__fecha_creacion_programa = fecha_creacion_programa
        self.__status_programa = status_programa
        self.__director = director
        self.__cursos=list(cursos) #agregacion


    def agregar_curso(self, curso):
        self.__cursos.append(curso)
    
    """def calcular_total(self):
        total = 0
        for curso in self._cursos:
            total += curso.nota
        return total"""
    
    """def __str__(self):
        cursos_str = ''
        for curso in self._cursos:
            cursos_str += curso.__str__() + '|'

        return f'Orden: {self._id_programa}, \nProductos: {cursos_str}'"""
   

    #Definir setter y getter
    def get_nombre_programa(self):
        return self.__nombre_programa

    def set_nombre_programa(self, nombre_programa):
        self.__nombre_programa = nombre_programa

    def get_fecha_creacion_programa(self):
        return self.__fecha_creacion_programa

    def set_fecha_creacion_programa(self, fecha_creacion_programa):
        self.__fecha_creacion_programa = fecha_creacion_programa

    def get_status_programa(self):
        return self.__status_programa

    def set_status_programa(self, status_programa):
        self.__status_programa = status_programa

    def get_director(self):
        return self.__director

    def set_director(self, director):
        self.__director = director

    #Definir property
    nombre_programa = property(get_nombre_programa, set_nombre_programa)
    fecha_creacion_programa = property(get_fecha_creacion_programa, set_fecha_creacion_programa)
    status_programa = property(get_status_programa, set_status_programa)
    director = property(get_director, set_director)

cur1=Curso("Calculo4", 5, 20,"Ingenieria civil",90)
ing1 =Programa("ingenieria_Civil", "12/12/12", "activo", "Juan", cur1)
ing2= Programa("Arquitectura", "12/15/16", "activo", "Juan", ["Calculo3", "fisica2"] )


print(ing1.__cursos)

print(ing2.nombre_programa)