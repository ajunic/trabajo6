import Factoria

#comprobacion del modulo principal
if __name__ == '__main__':
	mi_factoria = Factoria.Factoria()

	#Factoria, crea a una persona!
	persona = mi_factoria.crear_persona('E', 0, 0, 0, 0, 0, 0)
	#se ha creado una persona masculina
	print(persona)
	# print persona.get_nombre()
	# print persona.get_genero()