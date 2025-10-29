while True:

        edad = int(input("Introduce tu edad: "))
        if 1 <= edad <= 120:
            break
        else:
            print("Por favor, introduce una edad entre 1 y 120.")

if 1 <= edad <= 15:
    print("Eres niño/a")
elif 16 <= edad <= 21:
    print("Eres adolescente")
elif 22 <= edad <= 35:
    print("Eres joven")
elif 36 <= edad <= 50:
    print("Eres maduro/a")
elif 51 <= edad <= 60:
    print("Eres de mediana edad")
elif 61 <= edad <= 80:
    print("Eres mayor")
elif 81 <= edad <= 100:
    print("Eres viejo/a")
else:
    print("Eres centenario/a")