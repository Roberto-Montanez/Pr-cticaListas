#Escribe un programa que reciba del usuario un número entero que representa la cantidad de números 
#que va a ingresar. El programa deberá recibir esa cantidad de números enteros, los colocará en una 
#lista y la desplegará a pantalla. Posteriormente deberá construir una nueva lista, con el cuadrado de 
#cada uno de los elementos de la lista del usuario.
def main():
    #escribe tu código abajo de esta línea
    lista = []
    listaCuadrada = []
    a = int(input())
    if a>0 :
        for i in range(a):
            n = int(input())
            lista.append(n)
            listaCuadrada.append(n**2)    
    print(lista)
    print(listaCuadrada)
    

if __name__=='__main__':
    main()
