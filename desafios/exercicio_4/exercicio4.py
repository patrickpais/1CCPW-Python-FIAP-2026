n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

media = (n1+n2+n3+n4)/4

if media >= 7:
    print(f"Sua nota e {media:.2f}, você está APROVADO")
elif media >= 5 and media < 7:
    print(f"Sua nota é {media:.2f}, você está de RECUPERAÇÃO ")
else:
    print("Você foi REPROVADO")