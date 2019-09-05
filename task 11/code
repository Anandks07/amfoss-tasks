import turtle

gm = turtle.Screen()
gm.title("Pong by Anand")
gm.bgcolor("black")
gm.setup(width=800, height=600)
gm.tracer(0)

score1=0
score2=0

#player1
player1=turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.color("white")
player1.shapesize(stretch_wid=5, stretch_len=1)
player1.penup()
player1.goto(-350,0)

#player2
player2=turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.color("white")
player2.shapesize(stretch_wid=5, stretch_len=1)
player2.penup()
player2.goto(350,0)

#BALL
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=2
ball.dy=-2

#PEN

pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player 1:0 Player 2:0",align="center", font=("Courier", 24,"normal"))

#movement functions
def player1up():
    y=player1.ycor()
    y+=20
    player1.sety(y)

def player1down():
    y=player1.ycor()
    y-=20
    player1.sety(y)
    
def player2up():
    y=player2.ycor()
    y+=20
    player2.sety(y)

def player2down():
    y=player2.ycor()
    y-=20
    player2.sety(y)

#Keyboard binding
gm.listen()
gm.onkeypress(player1up,"w")
gm.onkeypress(player1down,"s")
gm.onkeypress(player2up,"Up")
gm.onkeypress(player2down,"Down")

#part of code that may trouble me
while True:
    gm.update()

    #Move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #Border probs
    if ball.ycor()>290:
          ball.sety(290)
          ball.dy*=-1
          
    if ball.ycor()<-290:
          ball.sety(-290)
          ball.dy*=-1

    if ball.xcor()>390:
          ball.goto(0,0)
          ball.dx*= -1
          score1+=1
          pen.clear()
          pen.write("Player 1:{} Player 2:{}".format(score1,score2),align="center", font=("Courier", 24,"normal"))

    if ball.xcor()<-390:
          ball.goto(0,0)
          ball.dx*= -1
          score2+=1
          pen.clear()
          pen.write("Player 1:{} Player 2:{}".format(score1,score2),align="center", font=("Courier", 24,"normal"))
          
    #Collisions

    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()< player2.ycor() +40 and ball.ycor()>player2.ycor()-40):
        ball.setx(340)
        ball.dx*= -1

    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()< player1.ycor() +40 and ball.ycor()>player1.ycor()-40):
        ball.setx(-340)
        ball.dx*= -1    
