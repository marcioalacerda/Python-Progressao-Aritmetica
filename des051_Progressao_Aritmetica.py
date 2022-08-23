'''Melhorando o programa, agora perguntando para o  usuário se ele quer que mostre mais algum termo. O programa encerra quando ele disser que não quer mostrar os termos.'''

print('{:=^31}'.format(' PROGRESSÃO ARITMÉTICA '))
print('{:=^31}'.format(' MOSTRE 10 TERMOS DA PA '))
p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
pa = p
termo = 1
print('{:2}º termo = {}'. format(termo, pa))
ctrl = 10
resp = 'S'
while resp !='N':
    while termo != ctrl:
        pa += r
        termo += 1
        print('{:2}º termo = {}'. format(termo, pa))
    resp = str(input('Voce gostaria que mostrasse mais termos? [S/N] ')).strip().upper()
    if resp == 'S':
        ctrl = int(input('Digite o termo seguinte: '))
print('Fim do programa!')
