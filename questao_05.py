def main():
    letra = input("Digite uma letra: ")
    letra = letra.upper()
    if letra  == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
        print('Vogal')
    else:
        print('Consoante')
    

if __name__ == '__main__':
    main()