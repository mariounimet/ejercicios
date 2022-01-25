#ejercicio 4
#A continuación se te presentan 5 códigos postales escritos en código Morse, 
# todos almacenados en un mismo string y separados por “*”. 
# Tu labor consiste en descifrar cuáles son los números que componen cada código.

mensaje = '...._ __... ..... ..___*.____ ___.. ___.. _____*_.... ..___ ...__ _....*..... __... .____ .____*___.. ...._ ____. ____.*'
numero = ''
contador = 0

for i in mensaje:
    if i == '.' or i == '_':
        numero += i
    elif i == ' ' or i == '*':

        if numero[0] == '.':
            for j in numero:
                if j == '.':
                    contador += 1
        elif numero[0] == '_':
            for j in numero:
                if j == '_':
                    contador += 2
                elif j == '.':
                    contador += 1

        print(contador % 10, end='')
        numero = ''
        contador = 0
        if i =='*':
            print('\n', end='')


