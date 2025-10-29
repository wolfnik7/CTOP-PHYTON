palabras = ""
contador = 0

while True:
    palabra = input("Introduce una palabra: ")
    if palabra == "" or palabra.strip().lower() == "basta":
        break
    if palabras == "":
        palabras = palabra
    else:
        palabras = palabras + " " + palabra
    print(palabras)
    contador += 1

print("Has soportado estoicamente", contador, "preguntas")
