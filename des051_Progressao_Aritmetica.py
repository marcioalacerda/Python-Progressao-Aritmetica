'''Programa que ler o primeiro termo e a razão de uma PA. No final, mostrar os 10 primeiro termos dessa progressão'''
print('{:=^31}'.format(' PROGRESSÃO ARITMÉTICA '))
print('{:=^31}'.format(' MOSTRE 10 TERMOS DA PA '))
p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
pa = p
termo = 1
print('{:2}º termo = {}'. format(termo, pa))
for c in range(1,10):
    pa += r
    termo += 1
    print('{:2}º termo = {}'. format(termo, pa))
