# Ingreso de Datos
P = float(input("Ingrese el precio de suscripción: "))
U = int(input("Ingrese el número de usuarios: "))
GT = float(input("Ingrese el gasto total: "))
Uanterior = float(input("Ingrese la utilidad del año anterior: "))

# Validación divisor
if Uanterior == 0:
    print("Error: La utilidad del año anterior no puede ser cero.")
else:
    # Cálculo de utilidades presentes
    Uactuales = P * U - GT
    razon = Uactuales / Uanterior

# Resultado
print(f"La razón entre utilidades actuales y anteriores es: {razon:.2f}")