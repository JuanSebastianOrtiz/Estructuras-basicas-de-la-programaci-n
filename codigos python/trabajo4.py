
if __name__ == '__main__':
	# programa que calcula el tiempo en llegar a la vel maxima la unidad de km/h a m/s //
	# desarrollado por :  juan sebastian ortiz ibarra /
	# fecha 19/02/2023//
	# version 1.0//
	# declaracion de las variables 
	vel1 = float()
	vel2 = float()
	t = float()
	r = float()
	# inicializacion de las variables
	vel1 = 0.0
	vel2 = 0.0
	r = 0.0
	t = 0.0
	# captura de datos //
	# vel final en km/h
	print("Cual es la velocidad final") #el dato es en km/h
	vel2 = float(input())
	print("cual es su aceleracion")
	r = float(input())
	print("cual es la velocidad inicial")
	vel1 = float(input())
	# procesos aritmeticos//
	vel2 = (vel2*1000)/3600 #conversion de km/h a m/s
	t = (vel2-vel1)/r   #formula de tiempo
	# impresion de resultados//
	print(" el tiempo que se demoro en alcanzara la velocidad maxima es : ",t," s")

