'''

numero1 = int(input("Escribe el primer numero: "))
numero1
numero2 = int(input("Perfecto, ahora escribe el segundo numero: "))
numero2

comando = str(input("""Gracias, has habilitado el menu de comandos.
1 - SUMAR escribe el comando "SUM".
2 - RESTAR escrbie el comando "REST".
3 - MULTIPLICAR escribe el comando "MULT".
Escribe alguna de ellas para ejecutar: """))
comando

if comando == "SUM":
    print("Comando SUMAR arroja como resultado:" , numero1 + numero2)
elif comando == "REST":
    print("Comando RESTAR arroja como resultado:" , numero1 - numero2)
elif comando == "MULT":
    print("Comando MULTIPLICAR arroja como resultado:" , numero1 * numero2)
else: 
    print("Has introducido un comando no valido, reinicia el programa.")
    
numero = int(input("Escribe un numero PAR: "))
while (numero % 2) != 0:
    numero = int(input("Escribe un numero PAR: "))
else: print("Perfecto!")

suma = 0
for numero in range(100):
    if (numero % 2) != 0:
        suma = numero + suma
print(f'La suma de todos los numeros enteros impares del 1 al 100 es {suma}')

numero1 = int(input("Escribe el primer numero: "))
numero1
numero2 = int(input("Segundo numero: "))
numero2
numero3 = int(input("Tercer numero: "))
numero3
numero4 = int(input("Cuarto numero: "))
numero4
lista=[ numero1 , numero2, numero3 , numero4];
print(f"La media aritmetica es {sum(lista)/len(lista)}, gracias!");

numeros = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
numero = int(input("Escribe un numero entre el 1 y el 9: "))
while (numero in numeros) == False:
    numero = int(input("Escribe un numero entre el 1 y el 9: ")) 
else:  print("Perfecto!")

lista1 = list(range(11))
print(lista1)
lista2 = list(range(-10,1,1))
print(lista2)

i = 0
lista3 = []
while i < 21:
    i += 1
    if (i % 2) == 0:
        lista3.append(i)
else: print(lista3)

i = -20
lista4 = []
while i < 0:
    i += 1
    if (i % 2) != 0:
        lista4.append(i)
else: print(lista4)

i = -20
lista4 = []
while i < 0:
    i += 1
    if (i % 2) != 0:
        lista4.append(i)
else: print(lista4)

i = 0
lista5 = []
while i < 51:
    i += 1
    last_digit = i % 10
    if last_digit == 0 or last_digit == 5:
        lista5.append(i)
    else: continue
else: print(lista5)

'''

lista_1 = ['h','o','l','a',' ', 'm','u','n','d','o']
lista_2 = ['h','o','l','a',' ', 'l','u','n','a']

lista_3 = []

for value in lista_1:
    if value in lista_3:
        pass
    else:
       lista_3.append(value)
for value in lista_2:
    if value in lista_3:
        pass
    else:
       lista_3.append(value)
print(lista_3)