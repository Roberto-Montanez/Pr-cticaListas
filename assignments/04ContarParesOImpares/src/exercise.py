#Desarrolla el programa que determine el total de valores pares e impares 
#de una lista de números enteros que recibirá en su entrada. 
#Los valores los captura el usuario uno por uno, se van almacenando en una lista y posteriormente 
#se analizará la lista para determinar cuantos valores pares e impares posee. Consideramos al 0 como par
def main():
    #escribe tu código abajo de esta línea
    lista = []
    pares = 0
    impares = 0
    a = str(input())
    while a != '*' :
        lista.append(a)
        e = int(a)
        if e%2==0 or e==0:
            pares = pares + 1
        elif e%2 != 0:
            impares = impares + 1
        a = str(input())
    print('PARES='+str(pares))
    print('IMPARES='+str(impares))
    

if __name__=='__main__':
    main()
