class seleccion(object):
    lista = None
    tam_lista = 0
    """docstring for seleccion."""
    def __init__(self,lista):
        self.lista = lista
        self.tam_lista = len(lista)

    def ordenar(self):
        i = 0
        print(self.lista)
        while i < self.tam_lista-1:
            min = i
            j = i+1
            while j < self.tam_lista:
                if self.lista[j] < self.lista[min]:
                    min = j
                j += 1
            tmp = self.lista[i]
            self.lista[i] = self.lista[min]
            self.lista[min] = tmp
            print(self.lista)
            i += 1
        return self.lista

    def ordenarRec(self,tam):
        if tam >= self.tam_lista:
            return self.lista
        else:
            min = tam
            j = tam+1
            while j < self.tam_lista:
                if self.lista[j] < self.lista[min]:
                    min = j
                j += 1
            tmp = self.lista[tam]
            self.lista[tam] = self.lista[min]
            self.lista[min] = tmp
            print(self.lista)
            return self.ordenarRec(tam+1)
