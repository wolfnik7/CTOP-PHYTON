
num = input("Introduce un número entero: ")
try:
    cadena_num = int(num)
    resultado = cadena_num + 10
    print("El número convertido de cadena a entero es:", cadena_num)
    print("Resultado:", resultado)
except ValueError:
    print("Error: la cadena introducida no es un entero válido.")
