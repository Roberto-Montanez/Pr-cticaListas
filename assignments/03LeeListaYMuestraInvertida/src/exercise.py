#El usuario ingrese la cantidad de n elementos que va a tener la lista 
#posteriormente el programa debe leer cada uno de los n elementos, línea por línea 
# y se van agregando a la lista.
def main():
    #escribe tu código abajo de esta línea
    n = 0
    lista = []
    i = 0
    indice = -1
    while n<1 :
        n = int(input('Cuál es la cantidad de elementos en la lista? '))
    while i<n :
        valor = int(input('Teclea un valor: '))
        lista.append(valor)
        i = i+1
    for k in range(len(lista)-1,-1,-1):
        print('Lista['+str(indice)+'] = '+str(lista[k]))
        indice = indice-1
    print(min(lista))
    print(max(lista))
    lista.sort()
    print(lista)

if __name__=='__main__':
    main()
