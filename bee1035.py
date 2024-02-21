'''
Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A, e a soma de C com D for maior que a soma de A e B e se C e D, ambos, forem positivos e se a variável A for par escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos".

Entrada
Quatro números inteiros A, B, C e D.

Saída
Mostre a respectiva mensagem após a validação dos valores.
'''

n = input().split()
a,b,c,d = n

somaCD = int(c) + int(d) 
somaAB = int(a) + int(b)
if int(b) > int(c) and int(d) > int(a) and somaCD > somaAB and int(c) > 0 and int(d) > 0 and int(a)%2 == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')

    
                