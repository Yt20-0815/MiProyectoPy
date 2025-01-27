#1 Leer un numero entero y determinar cuantos digitos tiene

numero = int (input("Ejercicio #1 ingresa el numero: "))
digitos = len(str(numero))
print(f"el numero tiene {digitos} digitos")

#2 leer un numero entero y determinar si es primo

numero = int (input("Ejercicio #2 ingresa el numero: "))
print(numero)

if numero < 2:
    print("el numero no es primo")
   
elif numero == 2:
    print("el numero es primo")

else:
    for i in range(2, numero):
        if numero % i == 0:
            print("el numero no es primo")
            break
    else:
        print("el numero es primo")


#3 Leer 4 enteros, almacenarlos en una lista y determinar en que posicion de la lista esta el mayor numero leido

numero = [2,4,6,7,3,6,0,9,8,6,4,2]

mayor = max(numero)
posicion = numero.index(mayor)

print(f" Ejercicio #3. El número más grande es {mayor} y está en la posición {posicion + 1}.")

#4 Del siguiente listado, eliminar cualquier duplicado:

numeros = [1,1,2,3,3,2,5,6,2,7,8,4,3,1]
no_duplicados = set(numeros)
print("Ejercicio #4")
print(no_duplicados)