'''Refazendoo programa usando while.'''
print('{:=^31}'.format(' PROGRESSÃO ARITMÉTICA '))
print('{:=^31}'.format(' MOSTRE 10 TERMOS DA PA '))
p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
pa = p
termo = 1
print('{:2}º termo = {}'. format(termo, pa))
while termo !=10:
    pa += r
    termo += 1
    print('{:2}º termo = {}'. format(termo, pa))
print('FIM')
