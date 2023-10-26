from datetime import datetime
def main():
    data = input("Digite uma data no formato d/m/a: ")
    try:
        datetime.strptime(data, "%d/%m/%Y")
        print("A data é válida.")
    except ValueError:
        print("A data não é válida.")

if __name__ == '__main__':
    main()