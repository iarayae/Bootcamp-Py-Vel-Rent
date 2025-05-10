# Ingreso de datos
P = float(input("Ingrese el precio de suscripción: "))
U = int(input("Ingrese el número de usuarios: "))
GT = float(input("Ingrese el gasto total: "))

# Cálculo de Utilidades
utilidades = P * U - GT

# Resultado
print(f"Las Utilidades del proyecto son: ${utilidades}")