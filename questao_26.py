def main():
    n1 = int(input("Digite o valor: "))

    if n1 < 10 or n1 > 600:
        print("Valor de saque fora dos limites permitidos.")
    else:
        notas100 = n1 // 100
        notas50 = (n1 % 100) // 50
        notas10 = ((n1 % 100) % 50) // 10
        notas5 = (((n1 % 100) % 50) % 10) // 5
        notas1 = (((n1 % 100) % 50) % 10) % 5

        print(f"Notas de 100 reais: {notas100}")
        print(f"Notas de 50 reais: {notas50}")
        print(f"Notas de 10 reais: {notas10}")
        print(f"Notas de 5 reais: {notas5}")
        print(f"Notas de 1 real: {notas1}")
        

if __name__ == '__main__':
    main()