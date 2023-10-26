def main():
    letra = input("Digite uma letra: ")

    if letra.upper()  == 'F':
        print('Feminino')
    elif letra.upper() == 'M':
        print('Masculino')
    else:
        print('Sexo inválido')
    

if __name__ == '__main__':
    main()