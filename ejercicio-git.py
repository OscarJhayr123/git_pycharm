texto = input("Introduce un texto: ")
posiciones = int(input("¿Cuántas posiciones quieres rotar? "))


posiciones = posiciones % len(texto)
resultado = texto[posiciones:] + texto[:posiciones]

print("Resultado:", resultado)

("""Modificacion para que el ususario pueda introducir el texto que queire y pueda elegir cuantas posiciones rotar
pull request hacia oscar """)