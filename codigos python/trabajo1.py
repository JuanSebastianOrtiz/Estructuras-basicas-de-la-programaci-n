 


# programa que calcula aceleracion atravez del tiempo //
# desarrorllador juan sebastian ortiz ibarra //
# fecha 19/02/2023//
# version 1.0//
if __name__ == '__main__':
	# declaracion de las variables// 
	vel1 = float()
	vel2 = float()
	t = float()
	r = float()
	#inicializacion de las variables 
	vel1 = 0.0
	vel2 = 0.0
	t = 0.0
	r = 0.0
	# captura de datos //
	print("Cual es la velocidad inicial")
	vel1 = input()
	print("Cual es la velocidad final")
	vel2 = input()
	print("intervalo de tiempo")
	t = float(input())
	# calculo de los valores tomados//
	r = (vel2-vel1)/t # formula de la aceleracion
	# impresion de resultado 
	print("la aceleracion es : ",r)


