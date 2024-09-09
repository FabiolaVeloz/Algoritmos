def calculate_total_pressure(M1, M2, m1, m2, V, T):
    # Constante de los gases en las unidades indicadas
    R = 0.082  # dm^3·atm·K^(-1)·mol^(-1)

    # Convertimos la temperatura de grados Celsius a Kelvin
    T_kelvin = T + 273.15

    # Usamos la fórmula dada para calcular la presión total
    P_total = ((m1 / M1) + (m2 / M2)) * R * T_kelvin / V

    return P_total


# Bucle para asegurarse de que el usuario ingrese valores numéricos válidos
while True:
    try:
        # Pedimos al usuario que ingrese los valores requeridos
        M1 = float(input("Ingrese la masa molar del primer gas (g/mol): "))
        M2 = float(input("Ingrese la masa molar del segundo gas (g/mol): "))
        m1 = float(input("Ingrese la masa del primer gas (g): "))
        m2 = float(input("Ingrese la masa del segundo gas (g): "))
        V = float(input("Ingrese el volumen del recipiente (dm^3): "))
        T = float(input("Ingrese la temperatura en grados Celsius (°C): "))

        # Validar que no haya valores negativos ni ceros
        if M1 <= 0 or M2 <= 0 or m1 <= 0 or m2 <= 0 or V <= 0:
            print("Error: Las masas molares, masas de gas, y el volumen deben ser mayores que cero.")
        else:
            break  # Salimos del bucle si la entrada es válida
    except ValueError:
        print("Error: Por favor, ingrese números válidos.")

# Llamada a la función para calcular la presión total
P_total = calculate_total_pressure(M1, M2, m1, m2, V, T)

# Mostrar el resultado
print(f"La presión total ejercida por los gases es: {P_total:.2f} atm")
