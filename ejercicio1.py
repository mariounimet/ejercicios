#ejercicio 1
#1.1. CUENTA BANCARIA
#Debes realizar un programa que ejecute las operaciones que se llevan a cabo en una cuenta bancaria.
#1. 2020/04/10: El saldo inicial es de $3480
#2. 2020/04/11: Se hace una compra en una tienda de ropa y se gastan $96
#3. 2020/04/17: Se cobran $1200 de salario
#4. 2020/04/30: Se cobra un 3% del saldo de la cuenta en intereses
#5. 2020/05/02: Se hace una compra en el supermercado y se gastan $51
#Como output se espera:
#- Mostrar la cantidad de dinero recibida/retirada.
#- Mostrar el saldo actual de la cuenta y la fecha, al iniciar el programa y cada vez que se
#realice una operación. Por ejemplo:
#Se han retirado $96.
#Saldo actual a la fecha (2020/04/11): ${saldo_restante}


saldo = 1000
fecha = '(2021/25/01)'


while True:
    
    print("saldo actual para la fecha", fecha, ': $', saldo, "\n")
    operacion = input("escoja el numero del tipo de operación que quiere realiar:\n1- cobro\n2- compra\n")
    
    if int(operacion) != 2 and int(operacion) != 1:
        print("escoja un numero valido")
        continue
    elif int(operacion) == 1:
        cantidad_cobrar = input("ingrese la cantidad a cobrar: $")
        proveniencia = input("indique la proveniencia de su cobro: ")
        saldo += int(cantidad_cobrar)
    else:
        cantidad_gastar = input("ingrese la cantidad a gastar: $")
        que_compra = input("indique que comprará: ")
        saldo -= int(cantidad_gastar)
        print("se gastan $", cantidad_gastar, "de comprar", que_compra)

    consulta = input('desea terminar de operar? \nyes, no\n')
    if consulta == 'yes':
        break 
    elif consulta == 'no':
        continue
    else:
        break
