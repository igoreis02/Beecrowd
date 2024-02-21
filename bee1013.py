'''
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:



Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".
'''

x = input().split()

a, b, c = x 

maiorAB = (int(a) + int(b) + abs(int(a)-int(b)))/2

maior = (int(c) + int(maiorAB) + abs(int(c)-int(maiorAB)))/2

maior = int(maior)

print('{} eh o maior'.format(maior))