def leer_bool(texto):
    return input(texto).strip().lower() == "true"

# Inputs
chips = float(input("Ingrese los chips base: "))
mult = float(input("Ingrese el mult base: "))
mano = int(input("Ingrese el tamaño de la mano: "))

mimo = int(input("Cantidad de Mimos: "))
baron = int(input("Cantidad de Barones: "))

plasma = leer_bool("¿Usar baraja Plasma? (True/False): ")

# Cartas en mano (High Card)
k = mano - 1

# Triggers (base + mimes + red seal)
triggers = mimo + 2

# Multiplicador total
multiplicador_total = 1.5 ** (k * triggers * (baron + 1))

# Aplicar a mult
mult_final = mult * multiplicador_total
chips_final = chips

# Resultado final
if plasma:
    total = (chips_final + mult_final) / 2
else:
    total = chips_final * mult_final

# Output
print("Cartas en mano:", k)
print("Triggers:", triggers)
print("Multiplicador:", multiplicador_total)
print("Mult final:", mult_final)
print("Resultado final:", total)