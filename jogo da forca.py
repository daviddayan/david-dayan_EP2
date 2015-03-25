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
if escolha[0]==" ":
    escolha=choice(linhas)
    linhas.remove(escolha)
    print(escolha)
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
p=0
x=dist+1
pos=p*x


for l in escolha:
    if escolha[0]==letra:
        
        tartaruga.penup()
        tartaruga.setpos(1*x,5)
        tartaruga.write(letra)
        
    if escolha[1]==letra:
        
        tartaruga.penup()
        tartaruga.setpos(2*x,5)
        tartaruga.write(letra)
        
    if escolha[2]==letra:
        
        tartaruga.penup()
        tartaruga.setpos(3*x,5)
        tartaruga.write(letra)
                
    if escolha[3]==letra:
        
        tartaruga.penup()
        tartaruga.setpos(4*x,5)
        tartaruga.write(letra)

    if escolha[4]==letra:
        
        tartaruga.penup()
        tartaruga.setpos(5*x,5)
        tartaruga.write(letra)
        
    if escolha[5]==letra:
        
        tartaruga.penup()
        tartaruga.setpos(6*x,5)
        tartaruga.write(letra)

    if escolha[6]==letra:
        
        tartaruga.penup()
        tartaruga.setpos(7*x,5)
        tartaruga.write(letra)

    if escolha[7]==letra:
        
        tartaruga.penup()
        tartaruga.setpos(8*x,5)
        tartaruga.write(letra)

    if escolha[8]==letra:
        
        tartaruga.penup()
        tartaruga.setpos(9*x,5)
        tartaruga.write(letra)

    if escolha[9]==letra:
        
        tartaruga.penup()
        tartaruga.setpos(pos,5)
        tartaruga.write(letra)
    else:
        tartaruga.penup()
        tartaruga.setpos(50,95)
        tartaruga.pendown()
        tartaruga.color("red")
        dist = 1
        angulo = 180-((150-2)*180)/150
            
        for i in range(150):
            tartaruga.left(angulo)  # Vira o angulo pedido
            tartaruga.forward(dist) # Avança a distancia pedida
        
    if tam>10:

        if escolha[10]==letra:
            
            tartaruga.penup()
            tartaruga.setpos(11*x,5)
            tartaruga.write(letra)
        else:
            tartaruga.penup()
            tartaruga.setpos(50,95)
            tartaruga.pendown()
            tartaruga.color("red")
            dist = 1
            angulo = 180-((150-2)*180)/150
            
            for i in range(150):
                tartaruga.left(angulo)  # Vira o angulo pedido
                tartaruga.forward(dist) # Avança a distancia pedida

    if tam>11:
            
        if escolha[11]==letra:
            
            tartaruga.penup()
            tartaruga.setpos(12*x,5)
            tartaruga.write(letra)
        else:
            tartaruga.penup()
            tartaruga.setpos(50,95)
            tartaruga.pendown()
            tartaruga.color("red")
            dist = 1
            angulo = 180-((150-2)*180)/150
            
            for i in range(150):
                tartaruga.left(angulo)  # Vira o angulo pedido
                tartaruga.forward(dist) # Avança a distancia pedida

    if tam>12:
                
            if escolha[12]==letra:
                
                tartaruga.penup()
                tartaruga.setpos(13*x,5)
                tartaruga.write(letra)
            else:
                tartaruga.penup()
                tartaruga.setpos(50,95)
                tartaruga.pendown()
                tartaruga.color("red")
                dist = 1
                angulo = 180-((150-2)*180)/150
            
                for i in range(150):
                    tartaruga.left(angulo)  # Vira o angulo pedido
                    tartaruga.forward(dist) # Avança a distancia pedida

    if tam>13:

        if escolha[13]==letra:
            
            tartaruga.penup()
            tartaruga.setpos(14*x,5)
            tartaruga.write(letra)
        else:
            tartaruga.penup()
            tartaruga.setpos(50,95)
            tartaruga.pendown()
            tartaruga.color("red")
            dist = 1
            angulo = 180-((150-2)*180)/150
            
            for i in range(150):
                tartaruga.left(angulo)  # Vira o angulo pedido
                tartaruga.forward(dist) # Avança a distancia pedida

    if tam>14:    
                        
        if escolha[14]==letra:
            
            tartaruga.penup()
            tartaruga.setpos(15*x,5)
            tartaruga.write(letra)
        else:
            tartaruga.penup()
            tartaruga.setpos(50,95)
            tartaruga.pendown()
            tartaruga.color("red")
            dist = 1
            angulo = 180-((150-2)*180)/150
            
            for i in range(150):
                tartaruga.left(angulo)  # Vira o angulo pedido
                tartaruga.forward(dist) # Avança a distancia pedida

    if tam>15:
 
        if escolha[15]==letra:
            
            tartaruga.penup()
            tartaruga.setpos(16*x,5)
            tartaruga.write(letra)
        else:
            tartaruga.penup()
            tartaruga.setpos(50,95)
            tartaruga.pendown()
            tartaruga.color("red")
            dist = 1
            angulo = 180-((150-2)*180)/150
            
            for i in range(150):
                tartaruga.left(angulo)  # Vira o angulo pedido
                tartaruga.forward(dist) # Avança a distancia pedida

    if tam>16:
        if escolha[16]==letra:
            
            
            tartaruga.penup()
            tartaruga.setpos(17*x,5)
            tartaruga.write(letra)
        else:
            tartaruga.penup()
            tartaruga.setpos(50,95)
            tartaruga.pendown()
            tartaruga.color("red")
            dist = 1
            angulo = 180-((150-2)*180)/150
            
            for i in range(150):
                tartaruga.left(angulo)  # Vira o angulo pedido
                tartaruga.forward(dist) # Avança a distancia pedida

    if tam>17:        
        if escolha[17]==letra:
            
            tartaruga.penup()
            tartaruga.setpos(18*x,5)
            tartaruga.write(letra)
        else:
            tartaruga.penup()
            tartaruga.setpos(50,95)
            tartaruga.pendown()
            tartaruga.color("red")
            dist = 1
            angulo = 180-((150-2)*180)/150
            
            for i in range(150):
                tartaruga.left(angulo)  # Vira o angulo pedido
                tartaruga.forward(dist) # Avança a distancia pedida
                

    letra = window.textinput("letra", "escolha letra")
window.exitonclick()       

        
# desenha os risquinhos

# repetição

# Pede letra para o usuário
    # se acertou, desenha a letra turtle.write
        # se palavra commpleta, acertou
    # Se errou, desenha mais uma parte do boneco
        # boneco completo, perdeu



window.exitonclick()