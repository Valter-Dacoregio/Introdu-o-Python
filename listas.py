# -*- coding: utf-8 -*-

minha_lista_1 = ["abacate","banana","caqui", "laranja", "melancia"]

print(minha_lista_1)

minha_lista_1.append("kiwi")

print(minha_lista_1)

if("abacate" in minha_lista_1):
	print("Abacate está na lista")


del minha_lista_1[2:]

print(minha_lista_1)

print("-----------------------")

lista1 = [124, 345, 5, 72, 46, 6, 7, 3, 1, 7,0]
lista2 = [124, 345, 5, 72, 46, 6, 7, 3, 1, 7,0]
lista3 = [124, 345, 5, 72, 46, 6, 7, 3, 1, 7,0]

print(lista1)
lista1.sort()
print(lista1)

print("-----------------------")
print("-----------------------")

print(lista2)
lista2 = sorted(lista2)
print(lista2)

lista2.sort(reverse=True)
print(lista2)

lista3.reverse()
print(lista3)

print("-----------------------")