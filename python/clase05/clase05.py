"""num = 5
while num > 0:
    print(f'{num}')
    num -= 1
print('Terminó el conteo!')

chance  = 1
while chance <= 3:
  txt = input("Escribe SI: ")
  if txt == "SI":
     print("Ok, lo conseguiste en el intento", chance)
     break
  chance += 1
else:
  print("Has agotado tus tres intentos")

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

n = 0
while n < 10:
    n += 1
    if n == 2:
        pass
    print('n vale' , n)


lista = [1,2,3,4,5]
for valor in lista:
    print('Soy un item de la lista y valgo', valor)

indice = 0
numeros = [0,1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
    numeros[indice] *= 5
    indice += 1
print(numeros) 


texto = 'Hola Mundo, estoy usando for en Python'
for lea in texto:
    print(lea)

for numero in range(10):
    print('Numero vale',numero)
else:
    print("Se terminó de iterar y numero vale: ", numero)
    """

for numero in range(10):
    if numero == 2:
        continue
    elif numero == 8:
        break
    else:
        print("Se terminó de iterar y numero vale: ", numero)







