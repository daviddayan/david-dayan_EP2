# -*- coding: utf-8 -*-

from random import choice

f = open("entrada.txt", encoding="utf-8")

linhas = f. readlines()


# abre janela do turtle,desenha a forca

import turtle               # Usa a biblioteca de turtle graphics
window = turtle.Screen()    # cria uma janela
window.bgcolor("lightblue")
window.title("Poligonos")

tartaruga   = turtle.Turtle()  # Cria um objeto "desenhador"
tartaruga.speed(5)  # define a velocidade
tartaruga.penup()       # Remova e veja o que acontece
tartaruga.setpos(-50,0)
tartaruga.pendown()
tartaruga.color("red")

dist = 200
angulo = 90

for i in range(1):
    tartaruga.left(angulo)  # Vira o angulo pedido
    tartaruga.forward(dist) # Avança a distancia pedida
    
#import turtle               # Usa a biblioteca de turtle graphics
#window = turtle.Screen()    # cria uma janela
window.bgcolor("lightblue")
window.title("Poligonos")

#tartaruga   = turtle.Turtle()  # Cria um objeto "desenhador"
tartaruga.right(90)
tartaruga.speed(5)  # define a velocidade
tartaruga.penup()       # Remova e veja o que acontece
#tartaruga.setx()
#tartaruga.sety()
#tartaruga.setpos(-50,200)

tartaruga.pendown()
tartaruga.color("red")

dist = 100
angulo = 0

for i in range(1):
    tartaruga.left(angulo)  # Vira o angulo pedido
    tartaruga.forward(dist) # Avança a distancia pedida
    
#import turtle               # Usa a biblioteca de turtle graphics
#window = turtle.Screen()    # cria uma janela
window.bgcolor("lightblue")
window.title("Poligonos")

#tartaruga   = turtle.Turtle()  # Cria um objeto "desenhador"
tartaruga.right(0)
tartaruga.speed(5)  # define a velocidade
tartaruga.penup()       # Remova e veja o que acontece
tartaruga.pendown()
#tartaruga.color("red")

dist = 60
angulo = 270

for i in range(1):
    tartaruga.left(angulo)  # Vira o angulo pedido
    tartaruga.forward(dist) # Avança a distancia pedida
    
window.exitonclick()

escolha = choice(linhas)

tam=len(escolha)

window.bgcolor("lightblue")
window.title("Poligonos")

tartaruga.setx(-10)
tartaruga.sety(0)

tartaruga.right(0)
tartaruga.speed(5)  # define a velocidade
tartaruga.penup()       # Remova e veja o que acontece
tartaruga.pendown()
tartaruga.color("red")

dist = 30
angulo = 0

for i in range(1):
    tartaruga.left(angulo)  # Vira o angulo pedido
    tartaruga.forward(dist) # Avança a distancia pedida

   
# desenha os risquinhos

# repetição

# Pede letra para o usuário
    # se acertou, desenha a letra turtle.write
        # se palavra commpleta, acertou
    # Se errou, desenha mais uma parte do boneco
        # boneco completo, perdeu


