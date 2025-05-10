import math

# Ingreso de datos
radio_km = float(input("Ingrese el radio del planeta en kilómetros: "))
g = float(input("Ingrese el valor de la constante gravitacional en m/s²: "))

# Transformación de km a metros
radio_m = radio_km * 1000

# Cálculo velocidad de escape
ve = math.sqrt(2 * g * radio_m)

# Resultado
print(f"La velocidad de escape es {ve:.1f} [m/s]")