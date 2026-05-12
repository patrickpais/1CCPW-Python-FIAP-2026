# EXERCICIO 4

# n = int(input("Digite a quantidade de número: "))
#
# vetor = []
#
# print(f"Digite os {n} números:")
# for i in range(n):
#     numeros = int(input(f"Posição [{i}]: "))
#     vetor.append(numeros)
#
# soma = 0
# for elemento in vetor:
#     soma += elemento
#
# print("-" * 20)
# print(f"Vetor preenchido: {vetor}")
# print(f"A somatória dos números é: {soma}")


# EXERCICIO 5

# nomes = []
# print("Digite os nomes (ou aperte Enter vazio para encerrar):")
# while True:
#     entrada = input("Digite o nome: ")
#
#     if entrada == "":
#         break
#     nomes.append(entrada)
# print("\n" + "=" * 20)
# print("Nomes em ordem inversa:")
#
# for nome in reversed(nomes):
#     print(nome)

# # EXERCICIO 6
# n = int(input("Digite o tamanho do vetor: "))
#
# vetor = []
#
# for i in range(n):
#     caractere = input(f"Digite o numero de caractere para a posição {i}: ")
#     vetor.append(caractere[0])
#
# print(f"Veto origial: {vetor}")
#
# for i in range(n // 2):
#     j = (n - 1) - i
#
#     vetor[i], vetor[j] = vetor[j], vetor[i]
#
# print(f"Vetor invertido: {vetor}")

# EXERCICIO 7

# import random
#
# linhas = 3
# colunas = 4
#
# matriz = []
#
# for i in range(linhas):
#     linha = []
#     for j in range(colunas):
#         valor = random.randint(1, 100)
#         linha.append(valor)
#
#     matriz.append(linha)
#
# print("--- Matriz 3x4 ---")
# for linha in matriz:
#     print(linha)

#  EXERCICIO 8

# matriz_a = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# matriz_b = [
#     [7, 8, 9],
#     [10, 11, 12]
# ]
#
# linhas = len(matriz_a)
# colunas = len(matriz_a[0])
#
# matriz_c = []
#
# for i in range(linhas):
#     linha_soma = []
#     for j in range(colunas):
#         soma_matriz = matriz_a[i][j] + matriz_b[i][j]
#         linha_soma.append(soma_matriz)
#
#     matriz_c.append(linha_soma)
#
# print("Matriz A + Matriz B = Matriz C")
# print("-" * 30)
#
# for linha in matriz_c:
#     print(linha)

temperaturas = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]
contador = 0

for i in range(len(temperaturas)):
    print(f"Pos: {i} -- Valor: {temperaturas[i]}")
sala = 0
maior_registro = 0
sala_registro = 0
for num in temperaturas:
    media = (num[0] + num[1] + num[2] + num[3]) / 4
    contador = 0
    for temp in num:
        if temp >= 33:
            contador += 1
    sala += 1
    print(f"Sala {sala+1}")
    print(f"Média: {media}")
    print(f"Registro crítico: {contador}")
    if contador > maior_registro:
        maior_registro = contador
        sala_registro = sala
print(f"Sala com maior risco: {sala_registro}")





