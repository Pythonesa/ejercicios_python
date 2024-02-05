notas = []

for i in range(3):
    notas.append(int(input("Ingresa una nota: ")))

print(f'Promedio: {sum(notas) / len(notas)}')