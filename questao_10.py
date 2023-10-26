def main():
    n1 = float(input("Produto 1: "))
    n2 = float(input("Produto 2: "))
    n3 = float(input("Produto 3: "))

    if n1 < n2 and n1 < n3:
        print("Produto 1 é o que deve ser comprado")
    elif n2 < n1 and n2 < n3:
        print("Produto 2 é o que deve ser comprado")
    elif n3 < n2 and n3 < n1:
        print("Produto 3 é o que deve ser comprado")

if __name__ == '__main__':
    main()