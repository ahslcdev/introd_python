def main():
    n1 = int(input("Número 1: "))
    n2 = int(input("Número 2: "))
    n3 = int(input("Número 3: "))
    lista = [n1, n2, n3]

    lista.sort(reverse=True)

    print("Os números em ordem decrescente é: ")
    for i in lista:
        print(i)
    

if __name__ == '__main__':
    main()