'''
Fazer um algoritmo que pergunte dois números e ao final apresente os seguintes valores: a soma dos dois
números, a subtração do primeiro pelo segundo número, a subtração do segundo pelo primeiro número, a
multiplicação entre os dois números, a divisão do primeiro pelo segundo número, e também o resto da divisão
do primeiro pelo segundo número.
'''

num1 = float(input("Digite um número:"))
num2 = float(input("Digite outro número:"))

soma = num1 + num2
sub1 = num1 - num2
sub2 = num2 - num1
mult = num1 * num2
div1 = num1 / num2
resto = num1 % num2

print(f"A soma dos dois números é = {soma}")
print(f"A subtração do primeiro pelo segundo número = {sub1}")
print(f"A subtração do segundo pelo primeiro número = {sub2}")
print(f"A multiplicação entre os dois números = {mult}")
print(f"A divisão do primeiro pelo segundo número = {div1}")
print(f"O resto da divisão do primeiro pelo segundo número = {resto}")