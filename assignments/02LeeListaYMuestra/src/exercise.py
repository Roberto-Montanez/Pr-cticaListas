#El usuario ingrese la cantidad de elementos que va a ingresar a la lista 
#posteriormente el programa debe leer cada uno de los elementos de la lista
#uno por línea y se van agregando a la lista.
def main():
    #escribe tu código abajo de esta línea
    n = 0
    suma = 0
    lista = []
    i = 0
    while n<1 :
        n = int(input('Cuál es la cantidad de elementos en la lista? '))
    while i<n :
        valor = int(input('Teclea un valor: '))
        suma = suma + valor
        lista.append(valor)
        i = i+1
    for i in range(len(lista)):
        print('Lista['+str(i)+'] = '+str(lista[i]))
    print(lista[-1])
    print(suma)
    print(suma/n)

if __name__=='__main__':
    main()
