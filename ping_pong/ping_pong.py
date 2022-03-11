import turtle
import os

wn = turtle.Screen()
wn.title("Ping_Pong by Abhay_Chandra")
wn.bgcolor("black")
wn.setup(width=800, height=620)
wn.tracer(0)

#Score 
score_a = 0
score_b = 0


#Paddle A
paddle_A = turtle.Turtle()
paddle_A.speed(0)
paddle_A.shape("square")
paddle_A.color("red")
paddle_A.shapesize(stretch_wid=5,stretch_len=1)
paddle_A.penup()
paddle_A.goto(-350,0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("yellow")
ball.speed(0)
ball.penup()
ball.goto(0,0)
ball.dx = 5
ball.dy = 5


# Scoring using pen
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player A:0 Player B:0", align="center", font=("Courier", 24, "normal"))

#Functions for moving
def paddle_a_up():
    y = paddle_A.ycor()
    y += 20 #add 20 pixels to y cord
    paddle_A.sety(y)
    
    
def paddle_a_down():
    y = paddle_A.ycor()
    y -= 20  # add 20 pixels to y cord
    paddle_A.sety(y)
    
    
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20  # add 20 pixels to y cord
    paddle_b.sety(y)
    
    
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20  # add 20 pixels to y cord
    paddle_b.sety(y)

#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w") #when user pres w move up paddle_a
wn.onkeypress(paddle_a_down, "s")#down on s
wn.onkeypress(paddle_b_up, "Up")  # when user pres w move up paddle_a
wn.onkeypress(paddle_b_down, "Down")  # down on s


#main game rule
while True:
    wn.update()#update the screen
    
    #moving ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    
    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        
    if ball.xcor() > 380:
        ball.goto(0,0)
        ball.dx *=-1
        score_a += 1
        score.clear()
        score.write("Player A:{} Player B:{}".format(score_a, score_b), align="center",
                    font=("Courier", 24, "normal"))
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        score.clear()
        score.write("Player A:{} Player B:{}".format(score_a, score_b), align="center",
                    font=("Courier", 24, "normal"))
        
    ##paddle ball collision
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor()<paddle_A.ycor() + 50 and ball.ycor()>paddle_A.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay ping_pong_sound.mp3&")
        
    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle_b.ycor()+50 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay ping_pong_sound.mp3&")
