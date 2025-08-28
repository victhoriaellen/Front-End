alturas = []
alturas_masculino = []
qtd_feminino = 0

for i in range(1, 16): 
    print(f"\nPessoa {i}:")
    altura = float(input("Digite a altura (em metros): "))
    genero = input("Digite o gênero (M para Masculino, F para Feminino): ").strip().upper()

    alturas.append(altura)

    if genero == "M":
        alturas_masculino.append(altura)
    elif genero == "F":
        qtd_feminino += 1
    else:
        print("Gênero inválido! Considerando como 'F'.")
        qtd_feminino += 1

maior_altura = max(alturas)
menor_altura = min(alturas)

if len(alturas_masculino) > 0:
    media_masculino = sum(alturas_masculino) / len(alturas_masculino)
else:
    media_masculino = 0

print("\n=== Resultados ===")
print(f"A maior altura do grupo: {maior_altura:.2f} m")
print(f"A menor altura do grupo: {menor_altura:.2f} m")
print(f"A média de altura dos homens: {media_masculino:.2f} m")
print(f"O número de mulheres: {qtd_feminino}")

