from seleccion import seleccion

def main():
    Lista = [9,8,7,6,5,4,3,2,1]
    selec = seleccion(Lista)

    print("Arreglo Desordenado: ", Lista)
    #print("Arreglo Ordenado: ", selec.ordenar())

    print("Arreglo Ordenado: ", selec.ordenarRec(0))



if __name__ == '__main__':
    main()
