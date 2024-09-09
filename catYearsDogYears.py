"""
Programa que calcula la edad de un perro y un gato en años humanos
"""

def calculate_pet_ages(human_years):
    # Inicialización de los años de gato y perro
    if human_years == 1:
        cat_years = 15
        dog_years = 15
    elif human_years == 2:
        cat_years = 15 + 9
        dog_years = 15 + 9
    else:
        # Para años mayores a 2, se suman los años correspondientes
        cat_years = 15 + 9 + (human_years - 2) * 4
        dog_years = 15 + 9 + (human_years - 2) * 5

    # Retornar los años en formato [humanYears, catYears, dogYears]
    return [human_years, cat_years, dog_years]


# Solicitar al usuario que ingrese los años humanos y validar la entrada
while True:
    try:
        # Intentar obtener la entrada del usuario y convertirla a entero
        human_years = int(input("Ingrese los años humanos (>= 1): "))

        # Validar que el valor sea mayor o igual a 1
        if human_years < 1:
            print("Por favor ingrese un número mayor o igual a 1.")
        else:
            break
    except ValueError:
        # Mostrar error si el usuario no ingresa un número entero válido
        print("Por favor ingrese un número entero válido.")

# Calcular los años de gato y perro
result = calculate_pet_ages(human_years)

# Imprimir el resultado
print(f"Años humanos: {result[0]}, Años del gato: {result[1]}, Años del perro: {result[2]}")