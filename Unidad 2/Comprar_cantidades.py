try:

    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))


    if num1 > num2:
        print("El 1º es mayor que el 2º")
    elif num2 > num1:
        print("El 2º es mayor que el 1º")
    else:
        print("Son iguales")

except ValueError:
    print("Error: No has introducido un valor de tipo numérico")
