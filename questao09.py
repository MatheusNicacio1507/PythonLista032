'''
Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a expressa apenas
em dias. Obs: Considere os anos com 365 dias e os meses com 30 dias.
'''

print("Informe os anos, meses e dias de sua idade ")
id_a = int(input("Quais os anos da sua idade? "))
id_m = int(input("Quantos meses completos já se passaram desde o seu aniversário? "))
dia = int(input("Quantos dias se passaram após o número de meses completos da resposta anterior? "))

ano = id_a * 365
mes = id_m * 30

total = ano + mes + dia
#ou total = (id_a * 365) + (id_m * 30) + dia
print(f"Sua idade em dias é de {total} dias")