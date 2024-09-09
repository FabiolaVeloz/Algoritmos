import math


def convert_to_16_9(x_res, y_res, constant):
    if constant == "height":
        # Mantener la altura constante
        new_x_res = math.ceil((16 / 9) * y_res)
        new_y_res = y_res

    elif constant == "width":
        # Mantener el ancho constante
        new_y_res = math.ceil((9 / 16) * x_res)
        new_x_res = x_res

    elif constant == "diagonal":
        # Mantener la diagonal constante
        diagonal = math.sqrt(x_res ** 2 + y_res ** 2)
        new_y_res = math.ceil(diagonal / math.sqrt((16 ** 2 + 9 ** 2)) * 9)
        new_x_res = math.ceil((16 / 9) * new_y_res)

    elif constant == "area":
        # Mantener el área constante
        area = x_res * y_res
        new_y_res = math.ceil(math.sqrt(area / (16 / 9)))
        new_x_res = math.ceil((16 / 9) * new_y_res)

    else:
        return "Error: La constante debe ser 'height', 'width', 'diagonal' o 'area'."

    return new_x_res, new_y_res


# Bucle para asegurarse de que el usuario ingrese números enteros válidos
while True:
    try:
        # Pedimos la resolución X y Y al usuario
        x_res = int(input("Ingrese la resolución X (ancho) actual: "))
        y_res = int(input("Ingrese la resolución Y (altura) actual: "))
        constant = input("Ingrese la constante (height, width, diagonal, area): ").lower()
        break  # Salimos del bucle si la entrada es válida
    except ValueError:
        # Si el usuario ingresa algo que no es un número entero, mostramos un error
        print("Error: Por favor, ingrese un número entero válido.")

# Llamamos a la función para convertir a una resolución de 16:9
result = convert_to_16_9(x_res, y_res, constant)

# Mostramos la nueva resolución si es válida
if isinstance(result, tuple):
    new_x_res, new_y_res = result
    print(f"La nueva resolución con relación de aspecto 16:9 es: {new_x_res}x{new_y_res}")
else:
    # Si hubo un error, se imprime el mensaje de error
    print(result)