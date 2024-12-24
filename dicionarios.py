meu_dicionario = {"A":"AMEIXA", "B":"BOLA", "C":"CACHORRO"}

print(meu_dicionario["A"])

print("-------------------")

for chave in meu_dicionario:
	print(chave + ":" + meu_dicionario[chave])

print("-------------------")

for i in meu_dicionario.items():
	print(i)

print("-------------------")

for i in meu_dicionario.values():
	print(i)

print("-------------------")

for i in meu_dicionario.keys():
	print(i)