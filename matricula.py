class Matricula:
    def _init_(self, fecha_matricula, hora_matricula):
        self._fecha_matricula = fecha_matricula
        self._hora_matricula = hora_matricula
    
    # fechaMatricula
    def getfecha_matricula(self):
        return self._fecha_matricula

    def setfecha_matricula(self, fechaM):
        self._fecha_matricula = fechaM

    # horaMatricula
    def gethora_matricula(self):
        return self._hora_matricula
    
    def sethora_matricula(self, horaM):
        self._hora_matricula = horaM

    # --------------------------------------------------
    def agregar_Curso(curso): #Devolvera None
        
        pass

    def agregar_Nota(nota): #Devolvera Int
        pass

    def total_vendido(precio): #Devolvera Float
        pass

    _fecha_matricula = property(getfecha_matricula, setfecha_matricula)
    _hora_matricula  = property(gethora_matricula, sethora_matricula)