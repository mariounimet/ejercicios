#ejercicio 5
#verificar que la palabra solo tenga letras y poner en mayusculas las vocales y en minuscula las consonantes:


from turtle import pos


word = input("inserte una palabra: ")
vocals = ['a', 'e', 'i', 'o', 'u']
new_word = ''

if word.isalpha() == True:
    word = word.lower()
    position = 0

    for i in word:
        if i in vocals:
            new_word += i.upper()
        else:
            new_word += i

    print(new_word)

