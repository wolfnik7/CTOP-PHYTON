try:
    entrada_usuario = input(" Introduce un número: ")
    numero = int(entrada_usuario)
except ValueError as e:
    print("Error: " , entrada_usuario , " no es un número entero válido.")
else:
    print("Correcto, " , numero , " es un número válido.")
finally:
    print("El programa ha terminado.")
