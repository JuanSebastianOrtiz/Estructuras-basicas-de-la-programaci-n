# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


# programa que calcula aceleracion atravez del tiempo //
# desarrorllador juan sebastian ortiz ibarra //
# fecha 19/02/2023//
# version 1.0//
if __name__ == '__main__':
	# definición de variables// 
	vel1 = float()
	vel2 = float()
	t = float()
	r = float()
	vel1 = 0.0
	vel2 = 0.0
	t = 0.0
	r = 0.0
	# toma de valores//
	print("Cual es la velocidad inicial")
	a = input()
	print("Cual es la velocidad final")
	b = input()
	print("intervalo de tiempo")
	t = float(input())
	# calculo de los valores tomados//
	r = (vel2-vel1)/t
	print("la aceleracion es : ",r)

