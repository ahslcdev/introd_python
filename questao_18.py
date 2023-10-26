def main():
    n1 = float(input("Digite o comprimento do primeiro lado 1: "))
    n2 = float(input("Digite o comprimento do segundo lado 2: "))
    n3 = float(input("Digite o comprimento do terceiro lado 3: "))

    if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
        if n1 == n2 == n3:
            tipo = "Equilátero"
        elif n1 == n2 or n1 == n3 or n2 == n3:
            tipo = "Isósceles"
        else:
            tipo = "Escaleno"
        
        print(f"Os lados formam um triângulo {tipo}.")
    else:
        print("Os lados não formam um triângulo.")
    
if __name__ == '__main__':
    main()