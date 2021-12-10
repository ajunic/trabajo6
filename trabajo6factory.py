class Persona:
    def factory (type):
        class Estudiante(Persona):
            def display(self):
                print("This is new Estudiante")

        class Profesor(Persona):
            def display(self):
                print("This is new Profesor")

        if(type == "Estudiante"):
            return Estudiante()
        elif (type == "Profesor"):
            return Profesor()

estudiante1 = Persona.factory("Estudiante")
estudiante1.display()

        