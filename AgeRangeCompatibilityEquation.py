"""
Programa que calcula la edad en compatibilidad para una edad ingresada
"""

import math


def age_compatibility_range(age):
    # Validación de la edad
    if age < 1 or age > 100:
        return "La edad debe estar entre 1 y 100."

    if age > 14:
        min_age = age // 2 + 7
        max_age = (age - 7) * 2
    else:
        min_age = math.floor(age - 0.10 * age)
        max_age = math.floor(age + 0.10 * age)

    return f"{min_age}-{max_age}"


# Solicitar la edad al usuario y realizar la validación
try:
    age = int(input("Ingrese su edad (entre 1 y 100): "))
    result = age_compatibility_range(age)
    print(f"El rango de edades compatibles para una cita es: {result}")
except ValueError:
    print("Por favor, ingrese un número entero válido.")