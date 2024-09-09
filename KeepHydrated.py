import math


def litres_needed(time):
    # Cada hora de ciclismo requiere 0.5 litros de agua
    litres = 0.5 * time

    # Redondeamos hacia abajo para obtener el valor entero más pequeño
    return math.floor(litres)


# Bucle para asegurar que el usuario ingrese un valor numérico válido
while True:
    try:
        # Pedimos al usuario que ingrese el tiempo de ciclismo en horas
        time = float(input("Ingrese el tiempo que Nathan pasó en bicicleta (en horas): "))

        # Validar que el tiempo sea positivo
        if time < 0:
            print("Error: El tiempo debe ser un número positivo.")
        else:
            break  # Salimos del bucle si la entrada es válida
    except ValueError:
        # Mostrar un mensaje de error si el valor ingresado no es numérico
        print("Error: Por favor, ingrese un número válido.")

# Llamada a la función para calcular los litros de agua necesarios
litres = litres_needed(time)

# Mostrar el resultado
print(f"Nathan beberá {litres} litros de agua.")