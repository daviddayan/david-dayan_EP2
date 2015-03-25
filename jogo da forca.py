# -*- coding: utf-8 -*-
from random import choice

f = open("entrada.txt", encoding="utf-8")

linhas = f. readlines()

#def desenha(tartaruga, n):
    

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
    

escolha = choice(linhas)
linhas.remove(escolha)

tam=len(escolha)

import turtle               # Usa a biblioteca de turtle graphics
#window = turtle.Screen()    # cria uma janela
window.bgcolor("lightblue")
window.title("Poligonos")

tartaruga   = turtle.Turtle()  # Cria um objeto "desenhador"
tartaruga.speed(5)  # define a velocidade
tartaruga.penup()       # Remova e veja o que acontece
tartaruga.setpos(0,0)
tartaruga.pendown()
tartaruga.color("red")

dist = 15
angulo = 0

for c in escolha:
    if c!= " ":
        tartaruga.left(angulo)  # Vira o angulo pedido
        tartaruga.forward(dist) # Avança a distancia pedida
    else:
        tartaruga.penup()
        tartaruga.left(angulo)  # Vira o angulo pedido
        tartaruga.forward(dist) # Avança a distancia pedida
        tartaruga.pendown()
        
    tartaruga.penup()
    tartaruga.forward(5)
    tartaruga.pendown()

    
erros=0
letra = window.textinput("letra", "escolha letra")
#p=escolha.index(letra)

x=dist+5
pos=p*x

#for l in escolha:
    
#        tartaruga.speed(1000)  # define a velocidade
#        tartaruga.penup()       # Remova e veja o que acontece
#        tartaruga.setpos(50,95)
#        tartaruga.pendown()
#        tartaruga.color("red")
#        n=150
#        dist = 1
#        angulo = 180-((n-2)*180)/n
#            
#        for i in range(n):
#            tartaruga.left(angulo)  # Vira o angulo pedido
#            tartaruga.forward(dist) # Avança a distancia pedida
        
if escolha[0]==letra:
    p=1
    tartaruga.penup()
    tartaruga.setpos(pos,5)
    tartaruga.write(letra)
    

if escolha[1]==letra:
    p=2
    tartaruga.penup()
    tartaruga.setpos(pos,5)
    tartaruga.write(letra)
    
    
if escolha[2]==letra:
    p=3
    tartaruga.penup()
    tartaruga.setpos(pos,5)
    tartaruga.write(letra)
    tartaruga.penup()
    tartaruga        
        
if escolha[3]==letra:
    p=4
    tartaruga.penup()
    tartaruga.setpos(pos,5)
    tartaruga.write(letra)
           

if escolha[4]==letra:
    p=5
    tartaruga.penup()
    tartaruga.setpos(pos,5)
    tartaruga.write(letra)
 

if escolha[5]==letra:
    p=6
    tartaruga.penup()
    tartaruga.setpos(pos,5)
    tartaruga.write(letra)
    

if escolha[6]==letra:
    p=7
    tartaruga.penup()
    tartaruga.setpos(pos,5)
    tartaruga.write(letra)
    

if escolha[7]==letra:
    p=8
    tartaruga.penup()
    tartaruga.setpos(pos,5)
    tartaruga.write(letra)
            

if escolha[8]==letra:
    p=9
    tartaruga.penup()
    tartaruga.setpos(pos,5)
    tartaruga.write(letra)
    
    
    
letra = window.textinput("letra", "escolha letra")
    


#for l in escolha:
 #   if l==letra:
        
# desenha os risquinhos

# repetição

# Pede letra para o usuário
    # se acertou, desenha a letra turtle.write
        # se palavra commpleta, acertou
    # Se errou, desenha mais uma parte do boneco
        # boneco completo, perdeu
window.exitonclick()