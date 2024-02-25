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
                matriz_1[i][j] = float(input("Ingrese el coeficiente de la variable" + str(j) + "de la ecuación" + str(i + 1) +": " ))






if __name__ == "__main__":
    main()