# coding=latin1
#Problema X
#Enforcado
#Terá de jogar este jogo com um amigo. Um introduz a palavra a encontrar e o
#outro tenta descobri-la
import cTurtle

def desenha_enforcado(i):
    cTurtle.up()
    if(i==0):
        cTurtle.goto(60,-90)
        cTurtle.setheading(180)
        cTurtle.down()
        cTurtle.forward(130)
        cTurtle.right(90)
        cTurtle.forward(160)
        cTurtle.right(90)
        cTurtle.forward(70)
        cTurtle.right(90)
        cTurtle.forward(20)
        cTurtle.up()
        cTurtle.goto(-70,50)
        cTurtle.down()
        cTurtle.goto(-50,70)
    elif(i==1):
        cTurtle.goto(-20,30)
        cTurtle.down()
        cTurtle.circle(20)
    elif(i==2):
        cTurtle.goto(0,10)
        cTurtle.down()
        cTurtle.goto(0,-30)
    elif(i==3):
        cTurtle.goto(0,0)
        cTurtle.down()
        cTurtle.goto(-20,-10)
    elif(i==4):
        cTurtle.goto(0,0)
        cTurtle.down()
        cTurtle.goto(20,-10)
    elif(i==5):
        cTurtle.goto(0,-30)
        cTurtle.down()
        cTurtle.goto(-20,-70)
        cTurtle.goto(-30,-70)
    elif(i==6):
        cTurtle.goto(0,-30)
        cTurtle.down()
        cTurtle.goto(20,-70)
        cTurtle.goto(30,-70)
    cTurtle.hideturtle()
    #cTurtle.mainloop()
        

def enforcado():
    jogar=1
    while jogar:
        palavra=raw_input('Palavra a descobrir: ')
        print "Vou agora limpar o ecrã"
        for i in range(80):
            print ""
        
        palavra=palavra.upper()
        resposta='_'*len(palavra)
        i=0
        desenha_enforcado(0)
        while (i<7) and (resposta!=palavra):
            letra=raw_input('Insira uma letra para a palavra -> '+resposta+'\n: ')
            letra=letra.upper()
            encontrou=0
            for j in range(len(palavra)):
                if palavra[j]==letra:
                    resposta=resposta[:j]+letra+resposta[j+1:len(resposta)] # a string é imutável
                    encontrou=1
            if encontrou==0:
                i=i+1
                desenha_enforcado(i)
        if resposta==palavra:
            print "Parabéns! Livrou-se da forca!!"
        else:
            print "Foi enforcado!!!!!!"
        resposta=raw_input("Quer jogar outra vez (S/N)? ")
        if resposta.upper()!='S':
            jogar=0
        else:
            cTurtle.reset()
                
    print 'Bye bye - faça Restart Shell agora'

        
        
