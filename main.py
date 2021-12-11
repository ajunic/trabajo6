from curso import *
from programa import *
from edificio import *


#Programa principal
"""Autores:-    
    -Juan David Arias
    -Juan David Lopez
    -Juan David Paredes
    -Juan David Ramirez
    -Juan David Sanchez
    -Juan David Torres
"""
print("Bienvenido al sistema mas mamalon de este curso de python avanzado")
print("Por favor ingrese los datos solicitados")
print("Siga las indicaciones para que el programa funcione correctamente")
print("Sigase las indicaciones para que el programa funcione correctamente ")

#variable de control para menu
print("Ingrese 1 para Servicios Docente \n 2 Para Servicios estudiantiles \n 3 Para Servicios administrativos \n 4 Para Salir")
digito=int(input("Ingrese un numero: "))

#menu de 4 opciones y sus subramas
while digito<=3:
    print("1 Verificacion Docente:")
    print("2 Confirmacion Estudiante:")
    print("3 Administracion:")
    print("4 Salir")
    digito=int(input("Ingrese un numero: "))
    
    #submenu de sercivios docente
    if digito==1:
        numero=0
        print("Bienvenido a Servicios Docente")
        #Menu de docente.
        while (numero<=3):
            print("\t MENU")
            print("1. Ingresar como docente:")
            print("2. Mostrar cursos a cargo de docente:")
            print("3. Salir")

            if numero==1:
                print("\t Registro de Docente")
            elif numero==2:
                print("\t Mostrar cursos a cargo de docente")
            elif numero==3:
                break

    
    
    #submenu de servicios estudiante
    elif digito==2:
        print("Bienvenido a Servicios Estudiantiles")
        while (numero<=3):
            print("\t MENU")
            print("1. Matricularse:")
            print("2. Mostrar cursos :")
            print("3. Salir")
            #Submenu de matricula
            if numero==1:
                print("\t MATRICULA")
                while (numero<=2):
                    print("\t MENU")
                    print("1. Pagar:")
                    print("2. Mostrar informacion cursos:")
                    print("3. Salir")

                    if numero==1:
                        pass #metdo para pagar
                    elif numero==2:
                        pass #metodo para mostrar informacion cursos
                    elif numero==3:
                        break

            elif numero==2:
                print("\t TUS CURSOS:")
                pass #metodo para mostrar cursos

            elif numero==3:
                break
    #submenu de servicios administrativos        
    elif digito==3:
        print("Bienvenido a Servicios Administrativos")
        while (numero<=3):
            print("\t MENU")
            print("1. Administrar Profesores:")
            print("2. Administrar Estudiantes:")
            print('3. Administrar Catalogos:')
            print("4. Salir")
        

            if numero==1:
                print("\t ADMINISTRAR PROFESORES")
                while (numero<=2):
                    print("\t MENU")
                    print("1.MOSTRAR PROFESORES:")
                    print("2.ELIMINAR PROFESORES:")
                    print("3. SALIR")

                    if numero==1:
                        pass #metodo para mostrar profesores
                    elif numero==2:
                        pass #delete profesores
                    elif numero==3:
                        break

            elif numero==2:
                print("\t ADMINISTRAR ESTUDIANTES")
                while (numero<=2):
                        print("\t MENU")
                        print("1.MOSTRAR ESTUDIANTES:")
                        print("2.ELIMINAR ESTUDIANTES:")
                        print("3. SALIR")

                        if numero==1:
                            pass #metodo para mostrar profesores
                        elif numero==2:
                            pass #delete profesores
                        elif numero==3:
                            break

            elif numero==3:
                print("\t ADMINISTRAR CATALOGOS")
                while (numero <= 2):
                        print("\t MENU")
                        print("1. Curos")
                        print("2. Aulas")
                        print("3. Tipos de profesores")
                        print('4. Edificio')
                        print('5. Turno')

                        if numero==1:
                            pass #metodo para mostrar profesores
                        elif numero==2:
                            pass #delete profesores
                        elif numero==3:
                            pass
                        elif numero==4:
                            Edificio.registrar_edificio()
                        elif numero==5:
                            break

            elif numero == 4:
                break


    elif digito==4:
        print("Gracias por usar nuestro sistema")
        break


#_______________________________________________________________________________

    


#Archivo madre para probar clases.

programa1=Curso("Curso de Python",5,20,"Informatica",90)
programa2=Curso("Curso de Java",5,20,"Informatica",99)
programa3=Curso("Curso de C#",5,20,"Informatica",100)
programa4=Curso("Curso de C++",5,20,"Informatica",80)

informatica=Programa("Ing Software",5,20,"Ing Jose")
ingcivil=Programa("Ing Civil",5,20,"Ing Jose")
ingelectrica=Programa("Ing Electrica",5,20,"Ing Jose")


informatica.agregar_curso(programa1)
informatica.agregar_curso(programa2)

informatica.mostrar_curso()
informatica.limitar_curso()

print(informatica.__dict__)






