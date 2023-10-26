def main():
    morangos = float(input("Quantos Kg de morangos foram adquiridos? "))
    macas = float(input("Quantos Kg de maçãs foram adquiridos? "))

    total = (morangos * 2.50) + (macas * 1.80)
    if (morangos + macas > 8) or (total > 25):
        desconto = 0.10
        total -= total * desconto

    print(f"Total a ser pago: R$ {total:.2f}")    

if __name__ == '__main__':
    main()