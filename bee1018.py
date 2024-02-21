'''
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.

'''

v = int(input())

print(v)
qtd100 = v // 100
v = v - qtd100 * 100

qtd50 = v//50
v = v - qtd50 * 50

qtd20 = v//20
v = v - qtd20 * 20
        
qtd10 = v//10
v = v - qtd10 * 10
    
qtd5 = v //5
v = v - qtd5 * 5

qtd2 = v// 2
v = v - qtd2 * 2

qtd1 = v // 1
v = v - qtd1 * 1

print('{} nota(s) de R$ 100,00'.format(qtd100))
print('{} nota(s) de R$ 50,00'.format(qtd50))
print('{} nota(s) de R$ 20,00'.format(qtd20))
print('{} nota(s) de R$ 10,00'.format(qtd10))
print('{} nota(s) de R$ 5,00'.format(qtd5))
print('{} nota(s) de R$ 2,00'.format(qtd2))
print('{} nota(s) de R$ 1,00'.format(qtd1))