def main():
    contador = 0

    n1 = input("Telefonou para a vítima? (Sim ou Não): ")
    n2 = input("Esteve no local do crime? (Sim ou Não): ")
    n3 = input("Mora perto da vítima? (Sim ou Não): ")
    n4 = input("Devia para a vítima? (Sim ou Não): ")
    n5 = input("Já trabalhou com a vítima? (Sim ou Não): ")

    if n1.lower() == "sim":
        contador += 1

    if n2.lower() == "sim":
        contador += 1

    if n3.lower() == "sim":
        contador += 1

    if n4.lower() == "sim":
        contador += 1

    if n5.lower() == "sim":
        contador += 1

    if contador == 2:
        classificacao = "Suspeita"
    elif contador in (3, 4):
        classificacao = "Cúmplice"
    elif contador == 5:
        classificacao = "Assassino"
    else:
        classificacao = "Inocente"

    print(f"Classificação: {classificacao}")

if __name__ == '__main__':
    main()