'''
Desenvolver um programa que pergunte ao usuário o seu peso (em quilos) e sua altura (em metros). Ao final o
programa deverá exibir na tela para o usuário o valor do peso informado em gramas e a altura em centímetros.
'''

peso_kg = float(input("Qual seu peso, em kg? "))
alt_m = float(input("Qual sua altura, em metros? "))

peso_g = peso_kg * 1000
alt_cm = alt_m * 100

print(f"Em gramas, você pesa: {peso_g}g")
print(f"Em centímetros, você mede: {alt_cm}cm")