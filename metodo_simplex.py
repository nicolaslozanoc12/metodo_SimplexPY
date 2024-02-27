global salidaaux
salidaaux = 1
matriz_1 = []
matriz_2 = []
lista = []
respuestas = {}

def ingresar_datos():
    global num_variable_Z
    global num_igualdades
    num_variable_Z = int(input("Ingrese el numero de variables: "))
    num_igualdades = int(input("Ingrese el numero de igualdades: "))
    global num_filas
    num_filas = num_igualdades + 1
    global num_colum
    num_colum = num_igualdades + num_variable_Z + 2

def crear_matriz(matriz):
    #crea la matriz con valores nulos
    for i in range(num_filas):
        matriz.append([])
        for j in range(num_colum):
            matriz[i].append(None)
    return matriz

def encontrar_col_piv(matriz):
    num_pivoteZ = 0
    global colum_pivote
    for i in range(num_colum):
        if matriz[num_filas - 1][i] < 0 and matriz[num_filas -1][i] <num_pivoteZ:
            num_pivoteZ = matriz[num_filas - 1][i]
            colum_pivote = i

def encontrar_elemento_piv(matriz):
    global fila_pivot
    num_menor = 100000
    for i in range(num_filas -1):
        if matriz[i][colum_pivote] == 0 or matriz[i][num_colum -1] / matriz[i][colum_pivote] < 0:
            continue
        else:
            if i == 0:
                num_menor = matriz[i][num_colum -1] / matriz[i][colum_pivote]
                fila_pivot = i
                elemento_pivote = matriz[i][colum_pivote]
            elif matriz[i][num_colum -1] / matriz[i][colum_pivote] < num_menor:
                num_menor = matriz[i][num_colum -1] /matriz[i][colum_pivote]
                fila_pivot = i
                elemento_pivote = matriz[i][colum_pivote]
    lista.append(fila_pivot)
    return elemento_pivote

def fila_entrante(matriz_nueva,matriz_vieja):
    for i in range(num_colum):
        matriz_nueva[fila_pivot][i] = matriz_vieja[fila_pivot][i] / elemento_pivote

def reorganizar_matriz(matriz_nueva):
    for i in range(num_filas):
        for j in range(num_colum):
            if i != fila_pivot:
                matriz_2[i][j] = matriz_1[i][j]-(matriz_1[i][colum_pivote]*matriz_2[fila_pivot][j])

def negativos(matriz_nueva):
    negativo = None
    for i in range(num_colum-1):
        if matriz_nueva[num_filas][i] < 0:
            salidaaux = 1
            negativo = matriz_nueva[num_filas-1][i]
        elif negativo == None:
            salidaaux = 0
    return salidaaux

def imprimir_matriz(matriz):
    for i in range(num_filas):
        tot = ""
        for j in range(num_colum):
            tot = tot + str(matriz[i][j]) + "   "
        print(tot)
    print()
def main():
    ingresar_datos()
    for i in range(num_filas):
        if i < num_filas-i:
            respuestas["S" + str(i+1)] = 0
        else:
            respuestas["Z"] = 0

    global matriz_1
    global matriz_2
    matriz_1 = crear_matriz(matriz_1)
    matriz_2 = crear_matriz(matriz_2)

    for i in range(num_filas):
        for j in range(num_colum):
            if j == 0 and i!= num_filas- 1:
                matriz_1[i][j] = 0
            elif j == 0 and i == num_filas-1:
                matriz_1[i][j] = 1
            elif 0 < j < num_variable_Z and i != num_filas - 1:
                matriz_1[i][j] = float(
                    input("Ingrese el coeficiente de la variable" + str(j) + "de la ecuación" + str(i + 1) +": " ))
            elif j == num_colum - 1 and i != num_filas - 1:
                matriz_1[i][j] = float(
                    input("Digite el coeficiente al que esta igualado la ecuacion " + str(i + 1) + ": "))
            elif 0 < j <= num_variable_Z and i == num_filas - 1:
                matriz_1[i][j] = float(input("Digite el coeficiente de la variable " + str(j) + " de la funcion Z: "))
                matriz_1[i][j] = matriz_1[i][j] * (-1)
            elif j == num_colum - 1 and i == num_filas - 1:
                matriz_1[i][j] = 0
            elif num_variable_Z < j < num_colum - 1:
                if i == j - num_variable_Z - 1:
                    matriz_1[i][j] = 1
                else:
                    matriz_1[i][j] = 0

    while salidaaux == 1:
        imprimir_matriz(matriz_1)
        encontrar_col_piv(matriz_1)
        global elemento_pivote
        elemento_pivote = encontrar_col_piv(matriz_1)
        fila_entrante(matriz_2, matriz_1)
        reorganizar_matriz(matriz_2)
        salidaaux = negativos(matriz_1)
        print(str(salidaaux))
        print(elemento_pivote)
        for i in range(num_filas):
            if i == fila_pivot:
                try:
                    respuestas["X" + str(i+1)] = respuestas.pop("S" + str(i+1))
                except:
                    respuestas["X" + str(i+1)] = matriz_2[i][num_colum - 1]
            elif i == num_filas -1:
                respuestas["Z"] =matriz_2[i][num_colum - 1]

        for i in range(num_filas):
            for j in range(len(lista)):
                if i == lista[j]:
                    respuestas["X" + str(i + 1)] = matriz_2[i][num_colum - 1]

        for i in range(num_filas):
            for j in range(num_colum):
                matriz_1[i][j] = matriz_2[i][j]
        for i in range(num_filas):
            for j in range(num_colum):
                matriz_2[i][j] = None
    print("respuesta: ")
    for key, value in respuestas.items():
        print(key + "=", value)




if __name__ == "__main__":
    main()