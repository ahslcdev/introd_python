def main():
    n1 = float(input("Salário: "))
    if n1 <= 280:
        percentual = 20
    elif 280 < n1 <= 700:
        percentual = 15
    elif 700 < n1 <= 1500:
        percentual = 10
    elif 1500 < n1:
        percentual = 5
    aumento = (n1 * percentual)/100

    print("Percentual aplicado: {}\nValor do aumento: {}\nNovo salário: {}\n".format(percentual, aumento, aumento + n1))
if __name__ == '__main__':
    main()