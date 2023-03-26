# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# programa que calcula el sueldo de empleados dependiendo de las horas diurnas y nocturnas trabajadas descontando el total al final //
	# desarrollado por :  juan sebastian ortiz ibarra //
	# fecha 19/02/2023//
	# version 1.0//
	# declaracion variables//
	a = float()
	b = float()
	c = float()
	pt = float()
	psd = float()
	d = float()
	n = str()
	# inicializacion de las variables
	a = 0.0
	b = 0.0
	c = 0.0
	pt = 0.0
	psd = 0.0
	d = 0.0
	n = ""
	# captura de datos//
	print("cual es su nombre ")
	n = input()
	print("cuanto le pagan por hora")
	a = float(input())
	print("cuantas horas diurnas trabajo")
	b = float(input())
	print("Cuantas horas nocturnas trabajo")
	c = float(input())
	# procesos aritmeticos//
	b = a*b #formula horas valor horas nocturnas
	c = a*c*1.40 # valor horas extras
	psd = b+c    # formula salario bruto 
	pt = psd*0.81  #formula pago total con el impuesto aplicado 
	d = psd-pt  # formula descuento 
	# impresion de resultados //
	print("trabajador con el nombre: ",n)
	print("el sueldo sin descuentos es: ",psd)
	print("su pago total es : ",pt)
	print("se descuento de su sueldo un valor de : ",d)

