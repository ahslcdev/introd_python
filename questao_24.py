
def main():
    n1 = int(input("Digite a idade do primeiro aluno: "))
    n2 = int(input("Digite a idade do segundo aluno: "))
    n3 = int(input("Digite a idade do terceiro aluno: "))

    media = (n1 + n2 + n3) / 3

    if media < 25:
        print("Turma Jovem")
    elif 25 <= media <= 40:
        print("Turma Adulta")
    else:
        print("Turma Idosa")

if __name__ == '__main__':
    main()