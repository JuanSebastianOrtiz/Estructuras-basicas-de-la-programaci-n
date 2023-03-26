 

if __name__ == '__main__':
	# programa que calcula aceleracion atravez del tiempo como la distancia recorrida en un intervalo de tiempo y transforma la unidad de km/h a m/s // de un cuerpo en reposo
	# desarrollador: juan sebastian ortiz ibarra //
	# fecha 19/02/2023//
	# version 1.0//
	# los resultados son en m/s//
	# declaracion de las variables
	vel1 = float()
	vel2 = float()
	t = float()
	r = float()
	d = float()
	# inicializacion de las variables
	vel1 = 0.0
	vel2 = 0.0
	t = 0.0
	r = 0.0
	d = 0.0
	# captura  de datos  
	print("Cual es la velocidad final")
	vel2 = float(input())      #no se toma la  velocidad inicial porque en el enunciado el camion esta en reposo 
	print("intervalo de tiempo")
	t = float(input())
	# procesos aritmeticos 
	r = (vel2-vel1)/t  # formula de la aceleracion
	d = (1/2*r)*(t*t) #formula de distancia 
	# impresion de resultado  
	print("la aceleracion es : ",r)
	print("la distancia recorrida es : ",d)

