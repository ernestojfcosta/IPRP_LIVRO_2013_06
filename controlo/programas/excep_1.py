# -*- coding: mac-roman -*-
# Tratamento de excepções

x=4

try:
	y=eval(input("\nDenominador: "))
	print(float(x) / y)
except ZeroDivisionError:
	print("\nCuidado: y nao pode ser zero!")
"As raizes do polinomio de coeficientes\
a=%d b=%d c= %d sao r1=%3.2f r2=%3.2f" % (a,b,c,r1,r2)