# -*- coding: utf-8 -*-

# VISUALIZAÇÃOD E DADOS EM PYTHON

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 0]
titulo = "Grafico de Barras"
eixoX = "Eixo X"
eixoY = "Eixo Y"

# Legendas
plt.title(titulo)
plt.xlabel(eixoX)
plt.ylabel(eixoY)

plt.plot(x, y)
plt.bar(x, y)
plt.show()




