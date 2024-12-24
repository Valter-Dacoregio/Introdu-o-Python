# -*- coding: utf-8 -*-

arquivo = open("arquivo.txt")

print("------------------")
print(arquivo)

print("------------------")
print(arquivo.read())

arquivo = open("arquivo.txt")
print("------------------")
linhas = arquivo.readlines()
print(linhas)
