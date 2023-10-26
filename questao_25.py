def main():
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))

    media = (n1+n2+n3)/3
    if 7.0 <= media < 10:
        print('Aprovado com média {}'.format(media))
    elif media < 7:
        print('Reprovado com média {}'.format(media))
    elif media == 10:
        print('Aprovado com distinção')
    

if __name__ == '__main__':
    main()