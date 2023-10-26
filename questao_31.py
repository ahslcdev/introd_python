def main():
    litros = float(input("Quantos litros foram vendidos? "))
    tipo_combustivel = input("Tipo de combustível (A - Álcool, G - Gasolina): ").upper()

    preco_alcool = 1.90
    preco_gasolina = 2.50
    desconto = 0

    if tipo_combustivel == "A":
        if litros <= 20:
            desconto = 0.03
        else:
            desconto = 0.05
        preco_final = litros * (preco_alcool - preco_alcool * desconto)
    elif tipo_combustivel == "G":
        if litros <= 20:
            desconto = 0.04
        else:
            desconto = 0.06
        preco_final = litros * (preco_gasolina - preco_gasolina * desconto)
    else:
        print("Tipo de combustível inválido.")
        preco_final = 0

    if preco_final > 0:
        print(f"Total a ser pago: R$ {preco_final:.2f}")


if __name__ == '__main__':
    main()