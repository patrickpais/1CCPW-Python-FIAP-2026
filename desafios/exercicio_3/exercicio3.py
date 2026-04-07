n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 == n2:
    print(f"Os números {n1} e {n2} são iguais")
elif n1 > n2:
    print(f"O {n1} é maior do que {n2}")
else:
    print(f"O {n2} é maior do que {n1}")