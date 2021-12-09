class Curso:
    def __init__(self,  nombre_curso, creditos, horas_semanales, programa,nota):
        self.nota = nota #agregada para punto 7
        self.nombre_curso = nombre_curso
        self.creditos = creditos
        self.horas_semanales = horas_semanales
        self.programa = programa

    def administrar_Curso(): #Devolvera None
        pass

    # define setter and getter methods for Curso attributes
    def get_nombre_curso(self):
        return self.nombre_curso

    def set_nombre_curso(self, nombre_curso):
        self.__nombre_curso = nombre_curso

    def get_creditos(self):
        return self.creditos

    def set_creditos(self, creditos):
        self.__creditos = creditos

    def get_horas_semanales(self):
        return self.horas_semanales

    def set_horas_semanales(self, horas_semanales):
        self.__horas_semanales = horas_semanales

    def get_programa(self):
        return self.programa

    def set_programa(self, programa):
        self.__programa = programa

    def get_nota(self):
        return self.nota

    def set_nota(self, nota):
        self.__nota = nota

    nombre_curso = property(get_nombre_curso, set_nombre_curso)
    creditos = property(get_creditos, set_creditos)
    horas_semanales = property(get_horas_semanales, set_horas_semanales)
    programa = property(get_programa, set_programa)
    nota = property(get_nota, set_nota)