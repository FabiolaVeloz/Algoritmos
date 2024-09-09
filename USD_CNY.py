def convert_usd_to_cny(usd):
    # Tasa de conversión: 1 USD = 6.75 CNY
    conversion_rate = 6.75

    # Conversión de USD a CNY
    cny = usd * conversion_rate

    # Devolver el valor de CNY formateado a 2 decimales con el texto 'Chinese Yuan'
    return f"{cny:.2f} Chinese Yuan"


# Bucle para asegurar que el usuario ingrese un número entero válido
while True:
    try:
        # Pedir al usuario que ingrese la cantidad de USD
        usd = int(input("Ingrese la cantidad de dólares estadounidenses (USD): "))
        break  # Salimos del bucle si el valor es un número entero válido
    except ValueError:
        # Mensaje de error si el valor ingresado no es un número entero
        print("Error: Por favor, ingrese un número entero válido.")

# Llamada a la función para convertir USD a CNY
result = convert_usd_to_cny(usd)

# Mostrar el resultado
print(result)