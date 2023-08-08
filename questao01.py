'''
Desenvolver um programa que pergunte o valor da conta a ser paga no restaurante e exiba como resposta o
valor com o acréscimo dos 10% da gorjeta do garçom.
'''

print("Qual o valor da conta a ser paga?")

conta = float(input("Insira o valor da conta: R$"))

garcom = conta * 10 / 100

conta = conta + garcom

print("Com o acréscimo de 10% para o garçom, você deve pagar: R$", conta)
