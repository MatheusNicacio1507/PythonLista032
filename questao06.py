'''
Fazer um algoritmo que pergunte o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por
ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas,
exibir ao final o seu nome, o salário fixo, a comissão e o salário completo (fixo + comissão sobre vendas) no final
do mês.
'''

nome = input("Qual seu nome? ")
sal = float(input("Qual o seu salário?"))
vendas = float(input("Qual o total de vendas no mês, em dinheiro?"))

comissao = vendas * 15/100

sal_total = sal + comissao

print(f"Seu nome é: {nome}")
print(f"Seu salário fixo é: R${sal}")
print(f"Sua comissão é: R${comissao}")
print(f"Seu salário completo é: R${sal_total}")

