def nba_extrap(ppg, mpg):
    # Si el número de minutos es 0, devolvemos 0 para evitar división por cero.
    if mpg == 0:
        return 0

    # Calculamos los puntos extrapolados a 48 minutos
    extrapolated_ppg = (ppg / mpg) * 48

    # Redondeamos el resultado a la décima más cercana
    return round(extrapolated_ppg, 1)


# Función para solicitar valores no negativos al usuario
def solicitar_valor(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("El valor no puede ser negativo. Intente de nuevo.")
            else:
                return valor
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")


# Solicitamos al usuario que ingrese los valores
ppg = solicitar_valor("Ingrese los puntos por juego (ppg): ")
mpg = solicitar_valor("Ingrese los minutos por juego (mpg): ")

# Llamamos a la función para calcular la extrapolación
resultado = nba_extrap(ppg, mpg)

# Mostramos el resultado
print(f"Los puntos extrapolados a 48 minutos son: {resultado}")
