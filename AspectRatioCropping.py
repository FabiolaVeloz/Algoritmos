import math

def convert_to_16_9(x_res, y_res):
    # Calculamos el nuevo ancho para la relación de aspecto 16:9, manteniendo la altura
    new_x_res = math.ceil((16 / 9) * y_res)
    return new_x_res, y_res

# Bucle para asegurarse de que el usuario ingrese números enteros válidos
while True:
    try:
        # Pedimos la resolución X y Y al usuario
        x_res = int(input("Ingrese la resolución X (ancho) actual: "))
        y_res = int(input("Ingrese la resolución Y (altura) actual: "))
        break  # Salimos del bucle si la entrada es válida
    except ValueError:
        # Si el usuario ingresa algo que no es un número entero, mostramos un error
        print("Error: Por favor, ingrese un número entero válido.")

# Llamamos a la función para convertir a una resolución de 16:9
new_x_res, new_y_res = convert_to_16_9(x_res, y_res)

# Mostramos la nueva resolución
print(f"La nueva resolución con relación de aspecto 16:9 es: {new_x_res}x{new_y_res}")