
''' Faça um algoritmo que leia 10 números inteiros e ao final apresente:
Quantidade de números pares digitados
Quantidade de números ímpares digitados
Quantidade de zeros digitados'''

pares = 0
impares = 0
zeros = 0

for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    
    if numero == 0:
        zeros += 1
    elif numero % 2 == 0:
        pares += 1
    else:
        impares += 1
s
print(f"Quantidade de números pares digitados foi: {pares}")
print(f"Quantidade de números ímpares digitados foi: {impares}")
print(f"Quantidade de zeros digitados foi: {zeros}")
