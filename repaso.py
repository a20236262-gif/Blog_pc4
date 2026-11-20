# Variables
nombre = "María"
edad = 22
promedio = 16.5
aprobado = True

# Mostramos en el terminal
print(nombre)
print(edad)
print(promedio)
print(aprobado)
print

# Consultamos tipos de datos
print(type(nombre))
print(type(edad))
print(type(promedio))
print(type(aprobado))

#nombre = input("Ingresa tu nombre: ")

#edad = int(input("Ingresa tu edad: "))

anio_nacimiento = 2026 - edad

print(f"Hola, {nombre}")
print(f"Naciste aproximadamente en {anio_nacimiento}")

nota = float(input("Ingresa tu nota: "))


if nota >= 11:
    print("Aprobado")
elif nota >= 0:
    print("Desaprobado")
else:
    print("Nota no válida")

# en el terminal: pip install pandas
import pandas as pd

datos = {
    "Lengua": ["Quechua", "Aimara", "Shipibo"],
    "Familia": ["Quechua", "Aimara", "Pano"]
}

df = pd.DataFrame(datos)

print(df)

# En el terminal : pip install matplotlib

import matplotlib.pyplot as plt

lenguas = ["Quechua", "Aimara", "Shipibo", "Ashaninka"]
valores = [15, 10, 8, 12]

plt.bar(lenguas, valores)

plt.title("Ejemplo de gráfico")
plt.xlabel("Lenguas")
plt.ylabel("Valores")

plt.show()