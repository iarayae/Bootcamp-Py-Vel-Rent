# Ingreso de datos
P = float(input("Ingrese el precio base de suscripción: "))
Unormal = int(input("Ingrese el número de usuarios normales: "))
Upremium = int(input("Ingrese el número de usuarios premium: "))
GT = float(input("Ingrese el gasto total: "))

# Cálculo de utilidades
utilidades = (P * Unormal) + (P * 1.5 * Upremium) - GT

# Resultado
print(f"Las utilidades del proyecto son: ${utilidades}")