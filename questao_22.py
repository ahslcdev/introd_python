def main():
    n1 = int(input("Digite um número: "))

    centenas = n1 // 100
    dezenas = (n1 % 100) // 10
    unidades = n1 % 10
    print(centenas, dezenas, unidades)
if __name__ == '__main__':
    main()