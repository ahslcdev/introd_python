def main():
    n1 = input("Digite um número: ")

    if '.' in n1:
        print('Número decimal')
    else:
        print('Número inteiro')

if __name__ == '__main__':
    main()