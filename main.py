from operations import *

print("CalculadoraPY")
print("________________")

nmr1 = int(input("Digite um numero: "))
nmr2 = int(input("Digite outro numero: "))

op = int(input("Com qual opcao voce deseja operar? \n1- + \n2- - \n3- * \n4-/\n "))

while (op >= 5) or (op <= 0):
    op = int(input("Com qual opcao voce deseja operar? \n1- + \n2- - \n3- * \n4-/\n "))

if op == 1:
    soma(nmr1, nmr2)

elif op == 2:
    subtr(nmr1, nmr2)

elif op ==3:
    multp(nmr1, nmr2)

else:
    div(nmr1, nmr2)