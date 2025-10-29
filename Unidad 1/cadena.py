texto = "Hola,aquí programando en Python"
vocales = "".join(c for c in texto if c.lower() in "aeiouáéíóú")
print("Las vocales son:", vocales)
