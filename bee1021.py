'''
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.
'''
v = float(input())

n100 = v // 100
v = v - n100 * 100

n50 = v // 50
v = v - n50 * 50

n20 =  v // 20
v = v - n20 * 20

n10 = v // 10
v = v - n10*10

n5 = v // 5
v = v - n5 * 5

n2 = v // 2
v = v - n2 * 2

m1 = float(v // 1.0)
v = float(v - m1 * 1.0)

m50 = float(v // 0.5)
v = float(v - m50*0.5)

m25 = float(v // 0.25)
v = float(v - m25*0.25)

m10 = float(v // 0.10)
v = float(v - m10*0.10)

m5 = float(v // 0.05)
v = float(v - m5*0.05)

m01 = float(v * 100)
m01 = float('%.2f' % m01)



print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(int(n100)))
print('{} nota(s) de R$ 50.00'.format(int(n50)))
print('{} nota(s) de R$ 20.00'.format(int(n20)))
print('{} nota(s) de R$ 10.00'.format(int(n10)))
print('{} nota(s) de R$ 5.00'.format(int(n5)))
print('{} nota(s) de R$ 2.00'.format(int(n2)))

print('MOEDAS:')
print('{} moeda(s) de R$ 1.00'.format(int(m1)))
print('{} moeda(s) de R$ 0.50'.format(int(m50)))
print('{} moeda(s) de R$ 0.25'.format(int(m25)))
print('{} moeda(s) de R$ 0.10'.format(int(m10)))
print('{} moeda(s) de R$ 0.05'.format(int(m5)))
print('{} moeda(s) de R$ 0.01'.format(int(m01)))