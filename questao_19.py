import math
def main():

    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"As raízes são: x1 = {x1} e x2 = {x2}")
    elif delta == 0:
        x1 = -b / (2*a)
        print(f"A raiz dupla é: x1 = {x1}")
    else:
        print("Não há raízes reais.")
if __name__ == '__main__':
    main()