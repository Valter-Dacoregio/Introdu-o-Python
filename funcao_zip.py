# -*- coding: utf-8 -*-

# ZIP

lista1 = [1, 2, 3, 4, 5, 6, 7]
lista2 = ["abacate", "bola","cachorro", "dinheiro", "elefante", "vaca"]
lista3 = ["R$ 2,00", "R$ 5,00", "Não tem preço", "Não tem preço", "Não tem preço", "Legal"]

for numero, nome, valor in zip(lista1, lista2, lista3):
	print(numero, nome, valor)


