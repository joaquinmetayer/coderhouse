a = 10
b = -5
c = "Hola"
d = [1, 2, 3]
e = (4,5,6) 

print(a * 5)  
print(a - b)    
print(c + "Mundo")   
print(c * 2)        
print(c[-1])        
print(c[1:])    
print(d + d)       
print(e[1])
print(e+(7,8,9))



numero_1 = 9
numero_2 = 3
numero_3 = 6

media = (numero_1 + numero_2 + numero_3) / 3
print("La nota media es", media)



nota_1 = 10
nota_2 = 7
nota_3 = 4

media_porcentual = (nota_1 * 0.15) + (nota_2 * 0.35) + (nota_3 * 0.50)
print("La nota media porcentual es", media_porcentual)


matriz = [ 
    [1, 5, 1],
    [2, 1, 2],
    [3, 0, 1],
    [1, 4, 4]
]
matriz_con_suma =[
    (matriz[0]+ [sum(matriz[0])]),
    (matriz[1]+ [sum(matriz[1])]),
    (matriz[2]+ [sum(matriz[2])]),
    (matriz[3]+ [sum(matriz[3])])
]
print(matriz_con_suma)