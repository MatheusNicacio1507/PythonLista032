'''
Escreva um algoritmo pergunte o número total de eleitores de um município, o número de votos brancos, nulos
e válidos e apresente como resposta o percentual que cada um representa em relação ao total de eleitores.
'''

eleitores = int(input("Qual o número total de eleitores? "))
branco = int(input("Qual o número de votos brancos? "))
nulo = int(input("Qual o número de votos nulo? "))
val = int(input("Qual o número de votos válidos? "))

brancop = branco * 100 / eleitores
nulop = nulo * 100 / eleitores
valp = val * 100 / eleitores

print(f"O percentual que a quantidade dos votos em brancos representam é = {brancop}%")
print(f"O percentual que a quantidade dos votos nulos representam é = {nulop}%")
print(f"O percentual que a quantidade dos votos válidos representam é = {valp}%")