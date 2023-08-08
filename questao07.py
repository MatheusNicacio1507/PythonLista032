'''
A Loja Mamão com Açúcar está vendendo seus produtos em até 10 prestações sem juros. Faça um algoritmo que
pergunte um valor de uma compra, o número de prestações escolhidas e apresente como resultado o valor das
prestações.
'''

valor = float(input("Qual o valor da compra? "))
prest = float(input("Qual o número de prestações escolhidas? "))
valor2 = valor / prest

print(f"O valor de cada prestaçãos é: R${valor2:.2f}")