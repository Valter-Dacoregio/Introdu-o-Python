# -*- coding: utf-8 -*-

# MAP

def dobro(x):
	return x*2


valor = 2
print(dobro(2))

print("----------------")

lista = [1,2,3,4,5]
print(dobro(lista))

print("----------------")

valor_dobrado = map(dobro, lista)
print(valor_dobrado) # NO PYTHON 3 IMPRIME APENAS O ENDEREÇO DE MEMÓRIA, NECESSÁRIO CONVERTER MAP PARA LIST

for v in valor_dobrado:
	print(v)

valor_dobrado = list(valor_dobrado)
print(valor_dobrado) 

print("----------------")