def main():
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))

    media = (n1+n2)/2
    if 7.0 <= media:
        print('Aprovado')
    elif 3 <= media <= 6.9:
        print('Em exame')
    else:
        print('Reprovado')
    

if __name__ == '__main__':
    main()