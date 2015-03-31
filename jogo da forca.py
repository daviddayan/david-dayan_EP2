# -*- coding: utf-8 -*-
from random import choice
import time
f = open("entrada.txt", encoding="utf-8")

linhas = f. readlines()
n=[]
for c in linhas:
    c2=c.strip()
    if c2!="":
        n.append(c2)

#def desenha(tartaruga, n):
    

# abre janela do turtle,desenha a forca
while len(n)>0:
    chutes=0
    acertos=0        
    erros=0
    
    import turtle               # Usa a biblioteca de turtle graphics
    
    window = turtle.Screen()    # cria uma janela
    window.bgcolor("lightblue")
    window.title("JOGO DA FORCA")
    
    window.clear()    
    
    tartaruga   = turtle.Turtle()  # Cria um objeto "desenhador"
    tartaruga.speed(5)  # define a velocidade
    tartaruga.width("8")
    tartaruga.penup()       # Remova e veja o que acontece
    tartaruga.setpos(-50,0)
    tartaruga.pendown()
    tartaruga.color("black")
    
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
    tartaruga.color("black")
    
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
        
    
    escolha = choice(n)
    n.remove(escolha)
    
    tam=len(escolha)
    
    import turtle               # Usa a biblioteca de turtle graphics
    #window = turtle.Screen()    # cria uma janela
    window.bgcolor("lightblue")
    window.title("JOGO DA FORCA")
    
    tartaruga   = turtle.Turtle()  # Cria um objeto "desenhador"
    tartaruga.speed(5)  # define a velocidade
    tartaruga.penup()       # Remova e veja o que acontece
    tartaruga.setpos(0,-15)
    tartaruga.pendown()
    tartaruga.color("red")
    tartaruga.width("2")
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
    
        
    
    
    #p=escolha.index(letra)
    
    x=dist
    
    
    def boneco():
        if erros==1:
            tartaruga.penup()
            tartaruga.setpos(50,95)
            tartaruga.pendown()
            tartaruga.color("red")
            dist = 1
            angulo = 180-((150-2)*180)/150
                
            for i in range(150):
                tartaruga.left(angulo)  # Vira o angulo pedido
                tartaruga.forward(dist) # Avança a distancia pedida
        if erros==2:
            tartaruga.penup()
            tartaruga.setpos(50,95)
            tartaruga.pendown()
            tartaruga.setpos(50,30)
        if erros==3:
            tartaruga.penup()
            tartaruga.setpos(50,85)
            tartaruga.pendown()
            tartaruga.setpos(20,60)
        if erros==4:
            tartaruga.penup()
            tartaruga.setpos(50,85)
            tartaruga.pendown()
            tartaruga.setpos(80,60)
        if erros==5:
            tartaruga.penup()
            tartaruga.setpos(50,30)
            tartaruga.pendown()
            tartaruga.setpos(20,0)
        if erros==6:
            tartaruga.penup()
            tartaruga.setpos(50,30)
            tartaruga.pendown()
            tartaruga.setpos(80,0)
            
    def desenhar_letra():
        n=0
        for i in range(len(escolha)):
            if letra == escolha[i]:
                tartaruga.penup()
                tartaruga.setpos((0+(i*20)),-10)
                tartaruga.pendown()
                tartaruga.write(letra , font = ('Arial',14,'normal'))
                n+=1
            if letra == "A" and escolha[i] == "Ã" or escolha[i]=="Â" :
                tartaruga.penup()
                tartaruga.setpos((0+(i*20)),-10)
                tartaruga.pendown()
                tartaruga.write(escolha[i] , font = ('Arial',14,'normal'))
                n+=1
            if letra == "E" and escolha[i] == 'É' or escolha[i]=='Ê':
                tartaruga.penup()
                tartaruga.setpos((0+(i*20)),-10)
                tartaruga.pendown()
                tartaruga.write(escolha[i] , font = ('Arial',14,'normal'))
                n+=1
            if letra == 'O' and escolha[i] == 'Ó' or escolha[i]=='Ô':
                tartaruga.penup()
                tartaruga.setpos((0+(i*20)),-10)
                tartaruga.pendown()
                tartaruga.write(escolha[i] , font = ('Arial',14,'normal'))
                n+=1
            if letra == 'I' and escolha[i] == 'Í':
                tartaruga.penup()
                tartaruga.setpos((0+(i*20)),-10)
                tartaruga.pendown()
                tartaruga.write(escolha[i] , font = ('Arial',14,'normal'))
                n+=1
        return n
    l=[]
    esp=escolha.count(" ")
    tentativas=0
    escolha=escolha.upper()        
    while erros < 6 and acertos < tam-esp:
        #if acertos < tam-esp:
            letra = window.textinput("letra", "escolha letra")
            letra=letra.upper()
            while letra in l:
                letra = window.textinput("letra", "escolha letra")
                letra=letra.upper()
            l.append(letra)
            tentativas+=1
            #pos=escolha.index(letra)
            tartaruga.penup()
            tartaruga.setpos(90,210)
            tartaruga.color("black")
            tartaruga.write("chutes errados", font = ("Arial",20,"normal"))
            if letra not in escolha:
                chutes+=1
                erros+=1
                
                tartaruga.penup()
                tartaruga.setpos(95+15*chutes,195)
                tartaruga.color("green")
                tartaruga.write(letra,font=("Arial",14,"normal"))
                tartaruga.color("red")
                boneco()
            else:
                acertos+=desenhar_letra()

    t=[]
    t.append(tentativas)
    soma=0
    for i in range(len(t)):
        soma+=t[i]
    if acertos==tam-esp:
        tartaruga.penup()
        tartaruga.color("black")
        tartaruga.setpos(85,120)
        tartaruga.write("PARABENS! VOCE ACERTOU A PALAVRA!")
        time.sleep(4)
    if erros==6:
        tartaruga.penup()
        tartaruga.color("black")
        tartaruga.setpos(85,120)
        tartaruga.write("VOCE ERROU A A PALAVRA E ESTA ENFORCADO!")
        time.sleep(4)
window.clear()
tartaruga.penup()
tartaruga.setpos(-200,70)
tartaruga.write("voce acertou:",font=("Arial",26,"normal"))
tartaruga.penup()
tartaruga.setpos(250,70)
tartaruga.write(acertos,font=("Arial",26,"normal"))
tartaruga.penup()
tartaruga.setpos(-200,35)
tartaruga.write("voce errou:",font=("Arial",26,"normal"))
tartaruga.penup()
tartaruga.setpos(250,35)
tartaruga.write(erros,font=("Arial",26,"normal"))
tartaruga.penup()
tartaruga.setpos(-200,0)        
tartaruga.write("chutes por palavra certa:",font=("Arial",26,"normal"))
tartaruga.penup()
tartaruga.setpos(250,0)
tartaruga.write(soma/acertos,font=("Arial",26,"normal"))

    


window.exitonclick()





