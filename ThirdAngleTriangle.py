def find_third_angle(angle1, angle2):
    # La suma de los ángulos internos de un triángulo es siempre 180 grados
    angle_sum = 180

    # Calculamos el tercer ángulo restando los otros dos del total
    third_angle = angle_sum - (angle1 + angle2)

    # Devolvemos el tercer ángulo
    return third_angle


# Bucle para asegurarse de que el usuario ingrese ángulos válidos (números enteros y positivos)
while True:
    try:
        # Pedir al usuario que ingrese los dos primeros ángulos del triángulo
        angle1 = int(input("Ingrese el primer ángulo del triángulo (en grados): "))
        angle2 = int(input("Ingrese el segundo ángulo del triángulo (en grados): "))

        # Validar que los ángulos sean positivos
        if angle1 <= 0 or angle2 <= 0:
            print("Error: Los ángulos deben ser números enteros positivos.")
        else:
            break  # Salimos del bucle si la entrada es válida
    except ValueError:
        # Mostrar un mensaje de error si los valores ingresados no son números enteros
        print("Error: Por favor, ingrese números enteros válidos para los ángulos.")

# Llamada a la función para calcular el tercer ángulo
third_angle = find_third_angle(angle1, angle2)

# Mostrar el resultado
print(f"El tercer ángulo del triángulo es: {third_angle} grados")