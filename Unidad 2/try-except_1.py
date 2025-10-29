texto=""

try:
    f = open("cuenta_atras.txt", "w")
    #texto = f.read()
    f.write("Hola,ke hase")
except Exception as e:
    print("Ocurrió un error: ",e)
else:
    print("Fichero escrito correctamente")
finally:
    f.close()