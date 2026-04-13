puntaje = float(input("Ingrese el puntaje base: "))
mano = int(input("Ingrese el tamaño de la mano: "))
mimo = int(input("Cantidad de Mimos: "))
baron = int(input("Cantidad de Barones: "))

# Cartas en mano (High Card)
k = mano - 1

# Triggers: base + mimes + red seal
triggers = mimo + 2

# Multiplicador total (Baron + Steel combinados)
multiplicador_total = 1.5 ** (k * triggers * (baron + 1))

# Puntaje final
total = puntaje * multiplicador_total

print("Cartas en mano:", k)
print("Triggers por carta:", triggers)
print("Multiplicador total:", multiplicador_total)
print("Puntaje final:", total)