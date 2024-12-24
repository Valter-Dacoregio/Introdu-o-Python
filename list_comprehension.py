# -*- coding: utf-8 -*-

x = [1,2,3,4,5,6,7,8,9]
y = []

print(x)

for i in x:
	y.append(i**2)

print(y)


print("------------------------")

# LIST COMPREHENSION

# PODEMOS FAZER DA SEGUINTE FORMA
# z = [valor_a_adicionar laço condição]
z = [i**2 for i in x]

print("USANDO LIST COMPREHENSION")
print(z)

print("------------------------")

a = [i for i in x if i%2==1]
print("ADICIONANDO NA NOVA LISTA SOMENTE ELEMENTOS ÍMPARES")
print(a)

print("------------------------")