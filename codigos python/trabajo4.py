# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


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
	# capturad de datos //
	# vel final en km/h
	print("Cual es la velocidad final")
	vel2 = float(input())
	print("cual es su aceleracion")
	r = float(input())
	print("cual es la velocidad inicial")
	vel1 = float(input())
	# procesos aritmeticos//
	vel2 = (vel2*1000)/3600
	t = (vel2-vel1)/r
	# impresion de resultados//
	print(" el tiempo que se demoro en alcanzara la velocidad maxima es : ",t," s")

