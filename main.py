from curso import *
from programa import *


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
    print(" 1 Verificacion Docente:")
    print("2 Confirmacion Estudiante:")
    print("3 Informe Administrativo:")
    print("4 Salir")
    digito=int(input("Ingrese un numero: "))

    if digito==1:
        print("Bienvenido a Servicios Docente")
    if digito==2:
        print("Bienvenido a Servicios Estudiantiles")
    if digito==3:
        print("Bienvenido a Servicios Administrativos")
    if digito==4:
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








