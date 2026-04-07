num_a = int(input("Digite o primeiro número: "))
num_b = int(input("Digite o segundo número: "))

if num_a%num_b == 0 or num_b%num_a == 0:
    print("Os números são Múltiplos")
else:
    print("Os números não são multiplos")