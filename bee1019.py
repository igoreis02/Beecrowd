'''
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.

'''

n = int(input())

h = n //3600
n = n - h * 3600

m = n // 60
n = n - m * 60

print('{}:{}:{}'.format(h,m,n))
