#Escribe un programa determine cuántas palabras de una lista empiezan con una determinada letra.
def main():
    #escribe tu código abajo de esta línea
    lista = []
    for i in range(5) : 
        a = input()
        lista.append(a)
    c = input() 
    for i in range(5) :
        b = list(lista[i])
        print(b)


if __name__=='__main__':
    main()
