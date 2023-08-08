'''
Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a expressa apenas
em dias. Obs: Considere os anos com 365 dias e os meses com 30 dias.
'''

print("Informe os anos, meses e dias de sua idade ")
id_a = int(input("Quais os anos da sua idade? "))
id_m = int(input("Quais os meses da sua idade? "))
dia = int(input("Quais os dias da sua idade? "))

ano = id_a * 365
mes = id_m * 30

total = ano + mes + dia

print(f"Sua idade em dias é de {total} dias")