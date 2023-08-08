'''
Fazer um algoritmo que receba o preço de custo de um produto e mostre como resposta o valor de venda. Sabese
que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário.
'''

preco = float(input("Qual o preço de custo do produto? "))
perc = float(input("Qual o percentual? "))

perc2 = preco * perc / 100

venda = preco + perc2

print(f"O valor da venda foi de: R${venda}")