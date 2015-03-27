# -*- coding: utf-8 -*-


from random import choice

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
    
    tartaruga   = turtle.Turtle()  # Cria um objeto "desenhador"
    tartaruga.speed(5)  # define a velocidade
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
    p=0
    x=dist
    pos=p*x
    
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

    esp=escolha.count(" ")
    print(esp)        
    while erros < 6 and acertos < tam-esp:
        #if acertos < tam-esp:
            letra = window.textinput("letra", "escolha letra")
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
                acertos+=1
                if escolha[0]==letra:
                
                    tartaruga.penup()
                    tartaruga.setpos(5,-11)
                    tartaruga.write(letra)
                
                if escolha[1]==letra:
                
                    tartaruga.penup()
                    tartaruga.setpos(2*x,-11)
                    tartaruga.write(letra)
                
                if escolha[2]==letra:
                    
                    tartaruga.penup()
                    tartaruga.setpos(3*x,-11)
                    tartaruga.write(letra)
                        
                if escolha[3]==letra:
                
                    tartaruga.penup()
                    tartaruga.setpos(4*x,-11)
                    tartaruga.write(letra)
        
                if escolha[4]==letra:
                
                    tartaruga.penup()
                    tartaruga.setpos(5*x,-11)
                    tartaruga.write(letra)
                
                if escolha[5]==letra:
                
                    tartaruga.penup()
                    tartaruga.setpos(6*x,-11)
                    tartaruga.write(letra)
        
                if escolha[6]==letra:
                    
                    tartaruga.penup()
                    tartaruga.setpos(7*x,-11)
                    tartaruga.write(letra)
                
                if tam>7:
                    
                    if escolha[7]==letra:
                
                        tartaruga.penup()
                        tartaruga.setpos(8*x,-11)
                        tartaruga.write(letra)
                
                if tam>8:
                    
                    if escolha[8]==letra:
                
                        tartaruga.penup()
                        tartaruga.setpos(9*x,-11)
                        tartaruga.write(letra)
                
                if tam>9:
        
                    if escolha[9]==letra:
                
                        tartaruga.penup()
                        tartaruga.setpos(10*x,-11)
                        tartaruga.write(letra)
        
                if tam>10:
        
                    if escolha[10]==letra:
                        
                        tartaruga.penup()
                        tartaruga.setpos(11*x,-11)
                        tartaruga.write(letra)
           
        
                if tam>11:
                    
                    if escolha[11]==letra:
                    
                        tartaruga.penup()
                        tartaruga.setpos(12*x,-11)
                        tartaruga.write(letra)
        
        
                if tam>12:
                            
                    if escolha[12]==letra:
                        
                        tartaruga.penup()
                        tartaruga.setpos(13*x,-11)
                        tartaruga.write(letra)
                 
        
                if tam>13:
        
                    if escolha[13]==letra:
                    
                        tartaruga.penup()
                        tartaruga.setpos(14*x,-11)
                        tartaruga.write(letra)
             
        
                if tam>14:    
                                
                    if escolha[14]==letra:
                
                        tartaruga.penup()
                        tartaruga.setpos(15*x,-11)
                        tartaruga.write(letra)
        
        
                if tam>15:
         
                     if escolha[15]==letra:
                    
                        tartaruga.penup()
                        tartaruga.setpos(16*x,-11)
                        tartaruga.write(letra)
        
        
                if tam>16:
                    if escolha[16]==letra:
                    
                    
                        tartaruga.penup()
                        tartaruga.setpos(17*x,-11)
                        tartaruga.write(letra)
        
        
                if tam>17:        
                    if escolha[17]==letra:
                    
                        tartaruga.penup()
                        tartaruga.setpos(18*x,-11)
                        tartaruga.write(letra)
                
                if tam>18:        
                    if escolha[18]==letra:
                    
                        tartaruga.penup()
                        tartaruga.setpos(19*x,-11)
                        tartaruga.write(letra)
                        
                if tam>19:        
                    if escolha[19]==letra:
                    
                        tartaruga.penup()
                        tartaruga.setpos(20*x,-11)
                        tartaruga.write(letra)
                        
                if tam>20:        
                    if escolha[20]==letra:
                    
                        tartaruga.penup()
                        tartaruga.setpos(21*x,-11)
                        tartaruga.write(letra)
        
    if acertos==tam-esp:
        tartaruga.penup()
        tartaruga.color("black")
        tartaruga.setpos(85,120)
        tartaruga.write("PARABENS! VOCE ACERTOU A PALAVRA!")
    if erros==6:
        tartaruga.penup()
        tartaruga.color("black")
        tartaruga.setpos(85,120)
        tartaruga.write("VOCE ERROU A A PALAVRA E ESTA ENFORCADO!")
    


    


window.exitonclick()