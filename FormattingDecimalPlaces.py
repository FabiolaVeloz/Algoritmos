def round_to_two_decimal_places(number):
    # Redondeamos el número a dos decimales
    return round(number, 2)

# Función para solicitar un número válido al usuario
def solicitar_numero():
    while True:
        try:
            # Solicitamos el número al usuario
            entrada = input("Ingrese un número válido: ")
            # Convertimos la entrada en un número flotante
            numero = float(entrada)
            return numero
        except ValueError:
            # Si la conversión falla, mostramos un mensaje de error
            print("Entrada inválida. Por favor, ingrese un número válido.")

# Solicitar el número al usuario
numero = solicitar_numero()

# Redondear el número a dos decimales y mostrar el resultado
resultado = round_to_two_decimal_places(numero)
print(f"El número {numero} redondeado a dos decimales es: {resultado}")
