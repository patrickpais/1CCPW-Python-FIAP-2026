nome = input("Digite seu primeiro nome: ") # str
nome2 = input("Digite seu sobrenome: ") # str


print(f'Bem-vindo(a) {nome} {nome2}')

print("-------------------------")

dia = int(input("Digite o dia do seu nascimento (DD): "))
mes = int(input("Digite o mes do seu nascimento (MM): "))
ano = int(input("Digite o ano do seu nascimento (AAAA): "))

idade = 2026 - ano
print("-----------IDADE--------------")
print(f'Sua data de nascimento é: {dia}/{mes}/{ano} e sua idade é: {idade}')
print("-------------------------")

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

total = n1 + n2
mult = n1 * n2
div = n1 / n2
sub = n1 - n2
print("-----------RESULTADOS--------------")
print(f'A soma desses números são: {total}')
print(f'A multiplicação desses números são: {mult}')
print(f'A divisão desses números são: {div}')
print(f'A subtração desses números são: {sub}')