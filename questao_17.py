def main():
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))

    media = (n1+n2)/2
    if 9 <= media <= 10:
        conceito = 'A'
    elif 7.5 <= media < 9:
        conceito = 'B'
    elif 6 <= media < 7.5:
        conceito = 'C'
    elif 4 <= media < 6:
        conceito = 'D'
    elif 0 <= media < 4:
        conceito = 'E'
    
    print('Nota 1: {}\nNota 2: {}\nMedia: {}\nConceito: {}\n'.format(n1, n2, media, conceito))
    if conceito in ['A', 'B', 'C']:
        print('Aprovado')
    elif conceito in ['D', 'E']:
        print('Reprovado')
    

if __name__ == '__main__':
    main()