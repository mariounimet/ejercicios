#ejercicio 3
#Una palabra o número palíndromo son aquellos que se leen igual de izquierda a derecha. 
# Por ejemplo: 101 es un número palíndromo, y 236 no lo es. Ana es una palabra palíndroma y pan no lo es.
#Diseña un programa que determine si un número o palabra ingresados por teclado, son palíndromos o no.


print("bienvenido: este programa esta hecho para determinar si una palabra o un numero son palíndromos")
palabra_num = input("ingrese numero o palabra a verificar: ")

verificar = True

for i in range(int(len(palabra_num)/2)):
    if palabra_num[i] == palabra_num[len(palabra_num) - 1 - i]:
        verificar = True
    else:
        print('la palabra o numero no es palindromo')
        verificar = False
        break
    
if verificar == True:
    print("la palabra o numero es palidromo")