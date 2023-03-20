# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# programa que calcula aceleracion atravez del tiempo como la distancia recorrida en un intervalo de tiempo y transforma la unidad de km/h a m/s //
	# desarrorllador juan sebastian ortiz ibarra //
	# fecha 19/02/2023//
	# version 1.0//
	# los resultados son en m/s//
	# declaracion de las variables
	vel1 = float()
	vel2 = float()
	t = float()
	r = float()
	d = float()
	# inicialización de las variables
	vel1 = 0.0
	vel2 = 0.0
	t = 0.0
	r = 0.0
	d = 0.0
	# captura  de datos  //
	print("Cual es la velocidad final")
	vel2 = float(input())
	print("intervalo de tiempo")
	t = float(input())
	# procesos aritmeticos //
	r = (vel2-vel1)/t
	d = (1/2*r)*(t*t)
	# impresion de resultado // 
	print("la aceleracion es : ",r)
	print("la distancia recorrida es : ",d)

