print("ANISE DE DADOS")
salario = float ( input ("informe seu salario:"))

if salario <= 1500:
	print("VOCÊ TEM UM SALARIO NORMAL, NÃO TEM COM SE PREOCUPAR")
elif salario > 2000 and salario <=3000:
	print("TA PODENDO EM")
elif salario > 3000 and salario <=4000:
	print("CLASSE ALTA")
elif salario > 4000 and salario <=6000:
	print("RICO")
elif salario > 4000 and salario <=9000:
	print("RICO CLASSE POBRE")
elif salario > 9000 and salario <=10000:
	print("RICO CLASSE BAIXA")
elif salario > 10000 and salario <=15000:
	print("RICO CLASSE MÉDIA")
elif salario > 15000 and salario <=20000:
	print("RICO CLASSE ALTA")
elif salario > 20000 and salario <=1000000:
	print("MILIONÁRIO")
else:
	print("ELO MUSK?")
