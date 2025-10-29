import time as t

try:
    N = int(input("Introduce un número entre 5 y 50: "))

    if not 5 <= N <= 50:
        print("Debes introducir un número entre 5 y 50.")
        exit(0)

    for i in range(N, 0, -1):
        print(i)
        t.sleep(0.5)

    print("¡Terminado!")

except ValueError:
    print("Error: Debes introducir un número válido, no una letra.")
