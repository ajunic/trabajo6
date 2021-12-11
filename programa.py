from curso import Curso


class Programa:
    def __init__(self,  nombre_programa, fecha_creacion_programa, status_programa, director, curso=[]):
        self.__nombre_programa = nombre_programa
        self.__fecha_creacion_programa = fecha_creacion_programa
        self.__status_programa = status_programa
        self.__director = director
        self.__curso=[] #agregacion


    def __str__(self):
        return self.__curso

    def agregar_curso(self, curso):
        self.__curso.append(curso.nombre_curso)

    def quitar_curso(self, curso):
        self.__curso.remove(curso)

       
    def mostrar_curso(self):
        for curso in self.__curso:
            print(curso)
        return self.__curso

    def limitar_curso(self):
        if len(self.__curso) < 3:
            print("El programa tiene mas de 3 cursos")
        else:
            print("El programa tiene menos de 3 cursos")
    

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


ing1 =Programa("ingenieria_Civil", "12/12/12", "activo", "Juan", ["Calculo2", "fisica"])
ing2= Programa("Arquitectura", "12/15/16", "activo", "Juan")
cur1=Curso("Calculo4", 5, 20,"Ingenieria civil",90)

print(ing1.director)

print(ing2.__dict__)
