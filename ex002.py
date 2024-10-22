'''Crie um programa que calcule e exiba na tela a média aritmética de um conjunto de 10 números lidos do usuário utilizando o laço de repetição for.'''

soma = 0

for i in range(10):
    numeros = int(input('Digite um numero: '))
    soma += numeros

media = soma / 10

print('A média é: ',media)
