print('---Exercicio1(Listas)---')
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
L.append(11)
print(f'com o 11: {L}')
L.remove(5)
print(f'Sem o 5: {L}')
L.reverse()
print(f'lista revertida: {L}\n')

print('---Exercicio2---')
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros.sort()
print(numeros)
sum(numeros)
print(sum(numeros))
min(numeros)
max(numeros)
print(f"Menor valor:{min(numeros)}, Maior valor:{max(numeros)}\n")

print('---Exercicio3---')
nomes=['Ana', 'Carlos', 'Beatriz', 'Daniel', 'Elisa']
print('Carlos' in nomes)
print(nomes.index('Beatriz'))
nomes[2]='Bruna'
print(f'A nova lista é: {nomes}\n')

print('---Exercicio1(Tuplas)---')
numeros = (10, 20, 30 , 40, 50)
terceiro_elemento = numeros[3]
print(f'Terceiro elemento: {terceiro_elemento}')
print('20' in numeros)
print(f'Conversão: {list(numeros)}\n')

print('---Exercicio2---')
cores = ('vermelho', 'azul', 'verde', 'amarelo', 'preto')
indice_verde = cores.index('verde')
print(f'O índice de cor verde: {indice_verde}')
quant_azul = cores.count('azul')
print(f'Quantidade de vezes da cor azul: {quant_azul}')
soma = cores + ('branco', 'cinza')
print(f'Nova lista: {soma}\n')

print('---Exercicio1(Dicionários)')
d ={'nome': 'João',
    'idade': 25,
    'cidade': 'São Paulo'}
print('Dicionário:', d)
#alterações
d['Profissão'] = 'Engenheiro'
d['idade'] = 26
del d['cidade']
#saida do novo dicionario
print('Novo dicionário:', d)