def main():
    letra = input("Digite o turno: ")
    letra = letra.upper()
    if letra  == 'M':
        print('Bom Dia!')
    elif letra  == 'V':
        print('Boa Tarde!')
    elif letra  == 'N':
        print('Boa Noite!')
    else:
        print('Valor inválido!')
    
if __name__ == '__main__':
    main()