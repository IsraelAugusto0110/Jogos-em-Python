#Pong utilizando linguagem Python

#01 inicio
import turtle as tr
#para tocar arquivo de audio quando a bola 'quicar'
import winsound as wns

#tela
wm = tr.Screen()
wm.title("Pong")
wm.bgcolor("black")
wm.setup(width=800, height=600)
wm.tracer(0)

#score
score_1 = score_2 = 0

#jogador 1
player_1 = tr.Turtle()
player_1.speed(0)
player_1.shape("square") #20px por 20px
player_1.color("white")
player_1.shapesize(stretch_wid=5, stretch_len=1)
player_1.penup()
player_1.goto(-350, 0)

#jogador 2
player_2 = tr.Turtle()
player_2.speed(0)
player_2.shape("square") #20px por 20px
player_2.color("white")
player_2.shapesize(stretch_wid=5, stretch_len=1)
player_2.penup()
player_2.goto(350, 0)

#bola
bola = tr.Turtle()
bola.speed(0)
bola.shape("square") #20px por 20px
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.dx = 0.1
bola.dy = 0.1

#Pen
pen = tr.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0 | Player 2: 0", align="center", font=("Courier",24, "bold"))

#funcoes

#mover jogador 1 para cima
def player_1_up():
    y = player_1.ycor()
    y+= 20
    player_1.sety(y)

#mover jogador 1 para baixo
def player_1_down():
    y = player_1.ycor()
    y-= 20
    player_1.sety(y)

#mover jogador 2 para cima
def player_2_up():
    y = player_2.ycor()
    y+= 20
    player_2.sety(y)

#mover jogador 2 para baixo
def player_2_down():
    y = player_2.ycor()
    y-= 20
    player_2.sety(y)

#lendo o teclado
wm.listen()
#jogador 1
wm.onkeypress(player_1_up, "w")
wm.onkeypress(player_1_down, "s")
#jogador 2
wm.onkeypress(player_2_up, "Up")
wm.onkeypress(player_2_down, "Down")

#game loop
while True:
    wm.update()

    #movendo a bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    #limite
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1
        wns.PlaySound("bounce.wav", wns.SND_ASYNC)

    if bola.xcor() > 390:
        bola.goto(0,0)
        bola.dx *= -1
        score_1 +=1
        pen.clear()
        pen.write("Player 1: {} | Player 2: {}".format(score_1, score_2), align="center", font=("Courier",24, "bold"))

    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1

    if bola.xcor() < -390:
        bola.goto(0,0)
        bola.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write("Player 1: {} | Player 2: {}".format(score_1, score_2), align="center", font=("Courier",24, "bold"))
        wns.PlaySound("bounce.wav", wns.SND_ASYNC)

    #testando colisao entre a bola e o jogador
    if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < player_2.ycor() + 50 
    and bola.ycor() > player_2.ycor() - 50):
        bola.setx(340)
        bola.dx *= -1
        wns.PlaySound("bounce.wav", wns.SND_ASYNC)

    if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < player_1.ycor() + 50 
    and bola.ycor() > player_1.ycor() - 50):
        bola.setx(-340)
        bola.dx *= -1
        wns.PlaySound("bounce.wav", wns.SND_ASYNC)