def suma():
    a=int(input("Ingrese el primer numero para sumar\n"))
    b=int(input("Ingrese el segundo numero para sumar\n"))
    total=a+b
    print(f"El resultado de la suma es {total}")
    
def resta():
    a=int(input("Ingrese el primer numero para restar\n"))
    b=int(input("Ingrese el segundo numero para restar\n"))
    total=a-b
    print(f"El resultado de la resta es {total}")
    
def multiplicacion():
    a=int(input("Ingrese el primer numero para multiplicar\n"))
    b=int(input("Ingrese el segundo numero para mulriplicar\n"))
    total=a*b
    print(f"El resultado de la multiplicacion es {total}")
    
def division():
    a=int(input("Ingrese el dividendo\n"))
    b=int(input("Ingrese el divisor (!=0)\n"))
    if b==0:
        print("El dividendo no puede ser 0")
    else:
        total=a/b
        print(f"El rsultado de la division es {total}")
        
def potencia():
    a=int(input("Ingrese la base\n"))
    b=int(input("Ingrese el exponente\n"))
    total=pow(a,b)
    print(f"El resultado de la potencicacion es {total}")
    
def factorial():
    a=int(input("Ingrese un numero para calcular su factorial\n"))
    total=1
    for i in range(1,a+1):
        total=total*i
    print(f"El factorial de {a} es {total}")
 
def raizCuadrada():
    a=int(input("Ingrese un numero para calcular su raiz cuadarda (debe ser entero positivo)\n"))
    if a<0 or a%1!=0:
        print("El numero debe ser un entero positivo")
    else:
        total=pow(a,0.5)
        print(f"La raiz cuadrada de {a} es {total}")



while True:
    opcion=int(input("\nSeleccione una operacion:\n1. Suma\n2. Resta\n3. Multiplicacion\n4. Division\n5. Potenciacion\n6. Factorial\n7. Raiz Cuadrada\n8. Salir\n"))
    if opcion==1:
        suma()
    elif opcion==2:
        resta()
    elif opcion==3:
        multiplicacion()
    elif opcion==4:
        division()
    elif opcion==5:
        potencia()
    elif opcion==6:
        factorial()
    elif opcion==7:
        raizCuadrada()
    elif opcion==8:
        break
    else:
        print("Ingrese una opcion valida\n")

        