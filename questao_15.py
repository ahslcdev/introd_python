def main():
    preco_custo = float(input("Digite o preço de custo do produto: R$ "))
    codigo_origem = int(input("Digite o código de origem (1 a 8): "))

    procedencia = {
        1: "Sul",
        2: "Norte",
        3: "Leste",
        4: "Oeste",
        5: "Nordeste",
        6: "Nordeste",
        7: "Centro-oeste",
        8: "Centro-oeste"
    }

    if codigo_origem in procedencia:
        origem = procedencia[codigo_origem]
        print(f"Preço com origem da {origem}: R$ {preco_custo:.2f}")
    else:
        print("Produto classificado como importado.")
    

if __name__ == '__main__':
    main()