def main():
    ano = int(input("Digite o ano: "))

    if ano % 4 == 0:
        print('Ano bissexto')
    else:
        print("Ano não é bissexto")
    

if __name__ == '__main__':
    main()