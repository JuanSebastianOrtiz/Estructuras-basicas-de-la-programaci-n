
if __name__ == '__main__':
	# programa que calcula la nota final de 3 parciales teniendo en cuenta sus porcentajes y especificando si aprobo o reprobo teniendo en cuenta la nota final y inasistencias //
	# desarrollado por : juan sebastian ortiz ibarra //
	# fecha 19/02/2023//
	# version 1.0//
	# Definicion de variables//
	n1 = float()
	n2 = float()
	n3 = float()
	p1 = float()
	p2 = float()
	p3 = float()
	i = float()
	nf = float()
	nombre = str()
	# inicializacion de las variables 
	n1 = 0.0
	n2 = 0.0
	n3 = 0.0
	p1 = 0.0
	p2 = 0.0
	p3 = 0.0
	i = 0.0
	nf = 0.0
	nombre = ""
	# captura de datos//
	print("cual es su nombre")
	nombre = input()
	print("    digite su primera nota: ")
	n1 = float(input())
	print("    digite su segunda nota: ")
	n2 = float(input())
	print("    digite su tercera nota: ")
	n3 = float(input())
	print("    digite porcentaje de la primera nota sin el simbolo %: ")
	p1 = float(input())
	print("    digite porcentaje de la segunda nota sin el simbolo %: ")  
	p2 = float(input())
	print("    digite porcentaje de la tercera nota sin el simbolo %: ")
	p3 = float(input())
	# operaciones aritmeticas//
	p1 = p1/100
	p2 = p2/100  # se divide entre 100 para dar como resultado los porcentajes para seguir operando 
	p3 = p3/100
	nf = (n1*p1)+(n2*p2)+(n3*p3) # formula de la nota final 
	# condicionales y impresion de resultados //
	print("Digite numero de inasistencias")
	i = float(input())
	if i<12:
		print("asistencias validas")    #se pierde por inasistencias => a 12 o por nota como se puede ver  en los condicionals por el contrario se gana 
	else:
		print("pierde por inasistencias")
	if nf>=3.5 and i<12:
		print("aprobado")
	else:
		print("reprobo")
	print("estudiante con nombre: ",nombre," su nota final es: ",nf)

