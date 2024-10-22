'''Foi realizada uma pesquisa de algumas características físicas da população de um certa região. Foram entrevistadas 15 pessoas e coletados os seguintes dados:  
a- sexo: M (masculino) e F (feminino)
b- cor dos olhos: A (azuis), V (verdes) e C (castanhos)
c- cor dos cabelos: L (loiros), C (castanhos) e P (pretos)
d- idade
Deseja-se saber:
A maior idade do grupo
A quantidade de indivíduos do sexo feminino, cuja idade está entre 18 e 35 anos e que tenham olhos verdes e cabelos louros.
A porcentagem de pessoas com os olhos azuis, verdes e castanhos
A porcentagem de Loiros, Castanhos e Pretos.
A porcentagem de pessoas do sexo masculino e feminino
'''

# Inicializando variáveis
maiorIdade = 0
femVerdesLouros = 0
olhosAzuis = 0
olhosVerdes = 0
olhosCastanhos = 0
cabLoiros = 0
cabCastanhos = 0
cabPretos = 0
masculino = 0
feminino = 0

# Loop para coletar dados de 15 pessoas
for i in range(15):
    sexo = input("Digite o sexo (M/F): ").upper()
    olhos = input("Digite a cor dos olhos (A - Azuis, V - Verdes, C - Castanhos): ").upper()
    cabelos = input("Digite a cor dos cabelos (L - Loiros, C - Castanhos, P - Pretos): ").upper()
    idade = int(input("Digite a idade: "))
    
    # Verifica a maior idade
    if idade > maiorIdade:
        maiorIdade = idade

    # Verifica o número de mulheres com olhos verdes, cabelos loiros e idade entre 18 e 35 anos
    if sexo == 'F' and olhos == 'V' and cabelos == 'L' and 18 <= idade <= 35:
        femVerdesLouros += 1

    # Contagem de cores dos olhos
    if olhos == 'A':
        olhosAzuis += 1
    elif olhos == 'V':
        olhosVerdes += 1
    elif olhos == 'C':
        olhosCastanhos += 1

    # Contagem de cores dos cabelos
    if cabelos == 'L':
        cabLoiros += 1
    elif cabelos == 'C':
        cabCastanhos += 1
    elif cabelos == 'P':
        cabPretos += 1

    # Contagem de sexo
    if sexo == 'M':
        masculino += 1
    elif sexo == 'F':
        feminino += 1

# Calculando porcentagens
total_pessoas = 15
porcentagemAzuis = (olhosAzuis / total_pessoas) * 100
porcentagemVerdes = (olhosVerdes / total_pessoas) * 100
porcentagemCastanhos = (olhosCastanhos / total_pessoas) * 100
porcentagemLoiros = (cabLoiros / total_pessoas) * 100
porcentagemCastanhosCabelos = (cabCastanhos / total_pessoas) * 100
porcentagemPretos = (cabPretos / total_pessoas) * 100
porcentagemMasculino = (masculino / total_pessoas) * 100
porcentagemFeminino = (feminino / total_pessoas) * 100

# Exibindo os resultados
print(f"\nMaior idade do grupo: {maiorIdade}")
print(f"Quantidade de mulheres entre 18 e 35 anos com olhos verdes e cabelos loiros: {femVerdesLouros}")
print(f"Porcentagem de pessoas com olhos azuis: {porcentagemAzuis:.2f}%")
print(f"Porcentagem de pessoas com olhos verdes: {porcentagemVerdes:.2f}%")
print(f"Porcentagem de pessoas com olhos castanhos: {porcentagemCastanhos:.2f}%")
print(f"Porcentagem de pessoas com cabelos loiros: {porcentagemLoiros:.2f}%")
print(f"Porcentagem de pessoas com cabelos castanhos: {porcentagemCastanhosCabelos:.2f}%")
print(f"Porcentagem de pessoas com cabelos pretos: {porcentagemPretos:.2f}%")
print(f"Porcentagem de pessoas do sexo masculino: {porcentagemMasculino:.2f}%")
print(f"Porcentagem de pessoas do sexo feminino: {porcentagemFeminino:.2f}%")

