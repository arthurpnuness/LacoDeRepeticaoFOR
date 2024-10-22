'''Faça um algoritmo que peça dois números para o usuário (o primeiro sempre será menor que o segundo), posteriormente apresente somente os números pares no intervalo entre os dois número. '''

num1 = int(input("Digite o primeiro número (menor): "))
num2 = int(input("Digite o segundo número (maior): "))

# Verifica se o primeiro número é menor que o segundo
if num1 < num2:
    print("Números pares no intervalo:")
    for numero in range(num1, num2 + 1):
        if numero % 2 == 0:
            print(numero)
else:
    print("O primeiro número deve ser menor que o segundo.")
