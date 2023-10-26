def main():
    valor_hora = float(input("Digite o valor da sua hora de trabalho: R$ "))
    horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

    salario_bruto = valor_hora * horas_trabalhadas

    if salario_bruto <= 900:
        ir_desconto = 0
    elif salario_bruto <= 1500:
        ir_desconto = salario_bruto * 0.05
    elif salario_bruto <= 2500:
        ir_desconto = salario_bruto * 0.10
    else:
        ir_desconto = salario_bruto * 0.20

    inss_desconto = salario_bruto * 0.10

    sindicato_desconto = salario_bruto * 0.03

    fgts = salario_bruto * 0.01

    total_descontos = ir_desconto + inss_desconto + sindicato_desconto

    salario_liquido = salario_bruto - total_descontos

    print("Salário Bruto: R$ {:.2f}".format(salario_bruto))
    print("(-) IR ({}%): R$ {:.2f}".format(int(ir_desconto / salario_bruto * 100), ir_desconto))
    print("(-) INSS (10%): R$ {:.2f}".format(inss_desconto))
    print("(-) Sindicato (3%): R$ {:.2f}".format(sindicato_desconto))
    print("FGTS (1%): R$ {:.2f}".format(fgts))
    print("Total de descontos: R$ {:.2f}".format(total_descontos))
    print("Salário Líquido: R$ {:.2f}".format(salario_liquido))


if __name__ == '__main__':
    main()