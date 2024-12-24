# -*- coding: utf-8 -*-

# w = open("arquivo2.txt", "w") # recria o arquivo
w = open("arquivo2.txt", "a") # grava ao final

w.write("Esse é o meu arquivo\n")
w.close()