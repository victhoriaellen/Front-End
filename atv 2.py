num_aulas = int(input("Digite o número de aulas do semestre: "))
faltas = int(input("Digite a quantidade de faltas do aluno: "))
nota1 = float(input("Digite a primeira nota (P1): "))
nota2 = float(input("Digite a segunda nota (P2): "))

percentual_presenca = ((num_aulas - faltas) / num_aulas) * 100

print("\nNúmero de aulas do semestre:", num_aulas)
print("Número de faltas do aluno:", faltas)
print(f"Percentual de presença do aluno: {percentual_presenca:.2f}%")

if percentual_presenca < 75:
    print("\nSituação final do aluno: Reprovado por falta")
else:
    media = (nota1 + nota2) / 2
    print("\nPrimeira nota:", nota1)
    print("Segunda nota:", nota2)
    
    if media >= 7:
        print(f"Média: {media:.2f}")
        print("Situação final do aluno: Aprovado")
    elif 5 <= media < 7:
        print(f"Média: {media:.2f}")
        nota_rec = float(input("Digite a nota da recuperação: "))
        media_final = (media + nota_rec) / 2
        print("Nota complementar (recuperação):", nota_rec)
        
        if media_final >= 5:
            print(f"Média final: {media_final:.2f}")
            print("Situação final do aluno: Aprovado na recuperação")
        else:
            print(f"Média final: {media_final:.2f}")
            print("Situação final do aluno: Reprovado na recuperação")
    else:
        print(f"Média: {media:.2f}")
        print("Situação final do aluno: Reprovado por nota")
