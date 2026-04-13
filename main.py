def leer_bool(texto):
    texto = input(texto).strip().lower()
    if texto == "y":
        return True
    elif texto == "n":
        return False
    else:
        raise ValueError("Entrada no válida. Por favor, ingrese 'y' o 'n'.")

# Inputs
nivel = int(input("Ingrese el nivel de hc: "))

chips = 5 + (nivel-1) * 5
mult = nivel
mano = int(input("Ingrese el tamaño de la mano: "))
mimo = int(input("Cantidad de Mimos: "))
baron = int(input("Cantidad de Barones: "))
plasma = leer_bool("¿Usar baraja Plasma? (y/n): ")

# Cartas en mano (High Card)
k = mano - 1

# Triggers (base + mimes + red seal)
triggers = mimo + 2

# Multiplicador total
multiplicador_total = mult * (1.5 ** (k * triggers * (baron + 1)))

# Resultado final
if plasma:
    total = (chips + multiplicador_total) / 2
else:
    total = chips * multiplicador_total

# Output
print("Cartas en mano:", k)
print("Triggers:", triggers)
print("Multiplicador:", multiplicador_total)
print("Resultado final:", total)