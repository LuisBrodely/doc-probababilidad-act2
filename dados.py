from tabulate import tabulate
from itertools import product

def calcular_salidas():
    objetos = []

    while True:
        tipo = input("¿Qué deseas usar: moneda, dado o ruleta? (Escribe 'salir' para terminar): ")
        if tipo.lower() == "salir":
            break

        objeto = {}
        objeto["tipo"] = tipo.lower()

        if objeto["tipo"] == "moneda":
            objeto["cantidad"] = 2
        else:
            cantidad = int(input("¿Cuántas caras o lados tiene el objeto?: "))
            objeto["cantidad"] = cantidad

        objetos.append(objeto)

    salidas_totales = 1
    opciones = [range(1, objeto["cantidad"] + 1) for objeto in objetos]
    resultados = list(product(*opciones))

    salidas_totales = len(resultados)

    return salidas_totales, resultados


salidas, combinaciones = calcular_salidas()

print("Tabla de combinaciones:")
headers = [f"Objeto {i + 1}" for i in range(len(combinaciones[0]))]
table = tabulate(combinaciones, headers=headers, tablefmt="grid")
print(table)

print("El número total de salidas posibles es:", salidas)

opcion = input("¿Deseas verificar si la suma de las salidas es par o impar? (Sí/No): ")
if opcion.lower() == "si":
    resultados_pares = []
    resultados_impares = []
    for combinacion in combinaciones:
        suma = sum(combinacion)
        if suma % 2 == 0:
            resultados_pares.append(combinacion + ("Par",))
        else:
            resultados_impares.append(combinacion + ("Impar",))

    print(f"Combinaciones con suma par ({len(resultados_pares)} combinaciones):")
    headers = [f"Objeto {i + 1}" for i in range(len(combinaciones[0]))]
    table_pares = tabulate(resultados_pares, headers=headers+["Resultado"], tablefmt="grid")
    print(table_pares)

    print(f"Combinaciones con suma impar ({len(resultados_impares)} combinaciones):")
    table_impares = tabulate(resultados_impares, headers=headers+["Resultado"], tablefmt="grid")
    print(table_impares)

opcion = input("¿Deseas verificar si la suma de las salidas es mayor a un número específico? (Sí/No): ")
if opcion.lower() == "si":
    numero = int(input("Ingresa el número a comparar: "))
    resultados_mayor = []
    for combinacion in combinaciones:
        suma = sum(combinacion)
        if suma > numero:
            resultados_mayor.append(combinacion + ("Mayor",))

    print(f"Combinaciones con suma mayor a {numero} ({len(resultados_mayor)} combinaciones):")
    headers = [f"Objeto {i + 1}" for i in range(len(combinaciones[0]))]
    table_mayor = tabulate(resultados_mayor, headers=headers+["Resultado"], tablefmt="grid")
    print(table_mayor)

opcion = input("¿Deseas verificar si la suma de las salidas es menor a un número específico? (Sí/No): ")
if opcion.lower() == "si":
    numero = int(input("Ingresa el número a comparar: "))
    resultados_menor = []
    for combinacion in combinaciones:
        suma = sum(combinacion)
        if suma < numero:
            resultados_menor.append(combinacion + ("Menor",))

    print(f"Combinaciones con suma menor a {numero} ({len(resultados_menor)} combinaciones):")
    headers = [f"Objeto dado{i + 1}" for i in range(len(combinaciones[0]))]
    table_menor = tabulate(resultados_menor, headers=headers+["Resultado"], tablefmt="grid")
    print(table_menor)
