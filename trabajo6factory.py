class Persona:
    def factory (type):
        class Estudiante(Persona):
            def display(self):
                print("This is new Estudiante")

        class Profesor(Persona):
            def display(self):
                print("This is new Profesor")

        