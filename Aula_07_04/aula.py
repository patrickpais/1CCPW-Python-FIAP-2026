'''
# Exemplo 1
idade = 18
tem_carteira = True

if idade >=18 or tem_carteira:
    print("Pode dirigir")
else:
    print("Não pode dirigir")
'''
#----------------------
'''
# Exemplo 2
nota = 5.5
frequencia = 50

if nota>=7 and frequencia >=75:
    print("Aprovado")
elif nota>=5 and frequencia >=75:
    print("Recuperação")
else:
    print("Reprovado")
'''
#----------------------
'''
# Exemplo 3
for i in range (5):
    print("Número é:", i)
'''
#----------------------
'''
# Exemplo 4
n = 0
while n < 5:
    print(n)
    n += 1
'''
#----------------------
'''
#Exemplo 5
def area_triangulo(b, h):
    return (b*h)/2
print(area_triangulo(2, 14))
'''
#---------------------
'''
#Exemplo 6
import math
def area_circunferencia(r):
    return math.pi * r**2
print(area_circunferencia(4))
'''
#---------------------
'''
#Exemplo 7 -
import os
print(os.getcwd())
'''
#---------------------
'''
# importar arquivos
#TXT
import pandas
dados1 = pandas.read_csv('DadosAula(2).txt ', sep=" ", header=0)
print(dados1)
'''
#---------------------
'''
#CSV
import pandas
dados2 = pandas.read_csv('DadosAula(2).csv', sep=";", header=0)
print(dados2)
'''
#---------------------

'''
#XLSX
import pandas
import openpyxl

dados3 = pandas.read_excel('DadosAula(2).xlsx', engine='openpyxl')
print(dados3)
'''
#---------------------

