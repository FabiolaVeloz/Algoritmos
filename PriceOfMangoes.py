"""
Programa que calcula el precio de los mangos en base a la promoción específicada
"""

def mango(quantity, price_per_mango):
    # Calculamos cuántos mangos se pagan
    paid_mangoes = (quantity // 3) * 2 + (quantity % 3)

    # Calculamos el costo total de los mangos pagados
    total_cost = paid_mangoes * price_per_mango

    return total_cost


# Bucle para asegurar que el usuario ingrese valores numéricos válidos
while True:
    try:
        # Pedir al usuario que ingrese la cantidad de mangos y el precio por mango
        quantity = int(input("Ingrese la cantidad de mangos: "))
        price_per_mango = float(input("Ingrese el precio por mango: "))

        # Validar que la cantidad y el precio sean positivos
        if quantity < 0 or price_per_mango < 0:
            print("Error: La cantidad y el precio deben ser números positivos.")
        else:
            break  # Salimos del bucle si los valores son válidos
    except ValueError:
        # Mostrar un mensaje de error si el valor ingresado no es numérico
        print("Error: Por favor, ingrese números válidos.")

# Llamada a la función para calcular el costo total de los mangos
total_cost = mango(quantity, price_per_mango)

# Mostrar el resultado
print(f"El costo total de los mangos es: ${total_cost:.2f}")