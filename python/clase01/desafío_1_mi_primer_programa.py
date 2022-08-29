# -*- coding: utf-8 -*-
"""Desafío 1 - Mi primer programa.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UlkZh2noVYlTVcvP94KTBhzRPeEmYvsu

# Desafío entregable 1

Crear un programa para calcular la nota final del estudiante en base a dos exámenes. Los exámenes cuentan con un porcentaje distinto de la nota final:

- **nota_1** cuenta como el 40% de la nota final
- **nota_2** cuenta como el 60% de la nota final

Aspectos a incluir:

- Tener en cuenta los temas vistos: números, print, input, variables, operaciones matemáticas, cadenas de texto. 
Aspectos a tener en cuenta:
- Los datos deben guardarse en variables y deben ser dinámicos por medio de input.
"""

nota_1 = float(input("Nota del 1º examen: "))
nota_2 = float(input("Nota del 2º examen: "))

nota_final = (nota_1 * 40 / 100) + (nota_2 * 60 / 100)
print("La nota final es:", nota_final)

nota_1 = input("Nota del 1º examen: ")
nota_1 = float(nota_1)
nota_2 = input("Nota del 2º examen: ")
nota_2 = float(nota_2)

nota_final = (nota_1 * 0.4) + (nota_2 * 0.6)
print("La nota final es: " + str(nota_final))

nota_1 = input("Nota del 1º examen: ")
nota_1 = float(nota_1)
nota_2 = input("Nota del 2º examen: ")
nota_2 = float(nota_2)

nota_final = (nota_1 * 0.4) + (nota_2 * 0.6)
print(f"La nota final es: {nota_final:0.2f}")