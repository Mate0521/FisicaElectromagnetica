import math

def calcular_potencial_esfera(q_nC, R_cm, r_cm):
    """
    Calcula el potencial eléctrico de una esfera con carga distribuida
    en su superficie.

    Variables:
        q_nC (float): Carga de la esfera en nanoCoulombs (nC).
        R_cm (float): Radio de la esfera en centímetros (cm).
        r_cm (float): Distancia desde el centro de la esfera en centímetros (cm).

    Retorna:
        float: Potencial eléctrico en Voltios (V).
    """

    # Constantes
    k = 8.9875e9  # Constante de Coulomb en N*m^2/C^2

    # Conversión de unidades al Sistema Internacional (SI)
    q = q_nC * 1e-9  # Convertir nC a Coulombs (C)
    R = R_cm / 100    # Convertir cm a metros (m)
    r = r_cm / 100    # Convertir cm a metros (m)

    potencial = 0.0

    if r > R:
        # Potencial afuera de la esfera (r > R)
        potencial = (k * q) / r
        print(f"\n--- Calculando Potencial AFUERA de la Esfera (r > R) ---")
        print(f"Distancia (r): {r_cm} cm (Afuera)")
    else:
        # Potencial adentro o en la superficie de la esfera (r <= R)
        potencial = (k * q) / R
        print(f"\n--- Calculando Potencial ADENTRO o en la SUPERFICIE de la Esfera (r <= R) ---")
        if r == R:
            print(f"Distancia (r): {r_cm} cm (En la Superficie)")
        else:
            print(f"Distancia (r): {r_cm} cm (Adentro)")

    print(f"Carga (q): {q_nC} nC")
    print(f"Radio de la esfera (R): {R_cm} cm")
    print(f"Potencial Eléctrico: {potencial:.4f} V")
    return potencial

# --- Valores constantes ---
Q_CONSTANTE_nC = 8  # Carga en nanoCoulombs
R_CONSTANTE_cm = 40 # Radio en centímetros

# --- Interacción con el usuario ---
print("--- Calculadora de Potencial Eléctrico para una Esfera Cargada en su Superficie ---")
print(f"Valores constantes: Carga (q) = {Q_CONSTANTE_nC} nC, Radio (R) = {R_CONSTANTE_cm} cm")

try:
    distancia_r_cm = float(input("Ingrese la distancia 'r' desde el centro de la esfera en cm: "))

    # Llamar a la función para calcular el potencial
    calcular_potencial_esfera(Q_CONSTANTE_nC, R_CONSTANTE_cm, distancia_r_cm)

except ValueError:
    print("Error: Por favor, ingrese un valor numérico válido para la distancia.")

# --- Verificación del programa para los valores especificados ---
print("\n--- Verificación del programa con valores predefinidos ---")

# r = 20 cm (adentro de la esfera)
print("\n--- Caso de prueba: r = 20 cm ---")
potencial_20cm = calcular_potencial_esfera(Q_CONSTANTE_nC, R_CONSTANTE_cm, 20)

# r = 60 cm (afuera de la esfera)
print("\n--- Caso de prueba: r = 60 cm ---")
potencial_60cm = calcular_potencial_esfera(Q_CONSTANTE_nC, R_CONSTANTE_cm, 60)