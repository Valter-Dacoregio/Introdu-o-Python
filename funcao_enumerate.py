# -*- coding: utf-8 -*-

# FUNÇÃO ENUMERATE

lista = ["abacate", "banana", "cachorro"]

for i in lista:
	print(i)

print("---------------")

for i in range(len(lista)):
	print(i, lista[i])

print("---------------")

for i, nome in enumerate(lista):
	print(i, nome)

print("---------------")