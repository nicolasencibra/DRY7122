as_privados = [
    range(64512, 65536),
    range(4200000000, 4294967295)
]

def es_as_privado(as_number):
    for rango in as_privados:
        if as_number in rango:
            return True
    return False

def main():
    try:
        as_number = int(input("Ingrese el número de AS de BGP: "))
        if es_as_privado(as_number):
            print(f"El AS {as_number} es un AS privado.")
        else:
            print(f"El AS {as_number} es un AS público.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()