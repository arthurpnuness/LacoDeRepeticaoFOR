'''Escreva um programa que imprima na tela a sequência de Fibonacci até o décimo termo utilizando o laço de repetição for.
'''

n1 = 0
n2 = 1

print(n1)
print(n2)

for i in range(2, 10):
    proxNum = n1 + n2
    print(proxNum)
    n1 = n2
    n2 = proxNum