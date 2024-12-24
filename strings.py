# -*- coding: utf-8 -*-

a = "Valter"
b = "Dacoregio"


concatenar = a + " " + b

print(concatenar)
print len(concatenar)

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])

print("------------------")
print(concatenar[0:])

print("------------------")
print(concatenar)
print(concatenar.lower())
print(concatenar.upper())


print("------------------")
seq = "  string com espaço em branco no início e no fim "
print(seq)
print(seq.strip())

print("------------------")
minha_string = "O rato roeu a roupa do rei de Roma"
print(minha_string)
minha_lista = minha_string.split(" ")
print(minha_lista)

busca = minha_string.find("rei")
print("Local onde inicia a palavra rei...: ")
print(busca)

print("------------------")
minha_string_alterada = minha_string.replace("rei", "rainha")
print("String altera...: " +  minha_string_alterada)
print("------------------")
print("------------------")
print("------------------")
print("------------------")







