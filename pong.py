import turtle
import time
window = turtle.Screen()
window.title("Pong By Aditya")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)


#left brick
brick_left = turtle.Turtle()
brick_left.speed(0)
brick_left.shape('square')
brick_left.color('red')
brick_left.shapesize(stretch_wid=5, stretch_len=1)
brick_left.penup()
brick_left.goto(-350,0)

#right Brick
brick_right = turtle.Turtle()
brick_right.speed(0)
brick_right.shape('square')
brick_right.color('blue')
brick_right.shapesize(stretch_wid=5, stretch_len=1)
brick_right.penup()
brick_right.goto(350,0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx = 0.1
ball.dy = 0.1

score_blue = 0
score_red = 0
#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
#moving left brick
def brick_left_up():
    y = brick_left.ycor()
    if y>=260:
        y+=0
    else:
        y+=20

    brick_left.sety(y)
        
def brick_left_down():
    y = brick_left.ycor()
    if y<=-260:
        y-=0
    else:
        y-=20

    brick_left.sety(y)

#moving right brick
def brick_right_up():
    y = brick_right.ycor()

    if y>=260:
        y+=0
    else:
        y+=20

    brick_right.sety(y)
        
def brick_right_down():
    y = brick_right.ycor()

    if y<=-260:
        y-=0
    else:
        y-=20

    brick_right.sety(y)


window.listen()
window.onkeypress(brick_left_up, 'w')
window.onkeypress(brick_left_down, 's')
window.onkeypress(brick_right_up, 'Up')
window.onkeypress(brick_right_down, 'Down')


while True:
    window.update()

    #upper boundary check
    if ball.ycor() >= 280:
        ball.dy *= -1
    elif ball.ycor() <=-280:
        ball.dy *= -1

    if ball.xcor()>= 400:
        ball.goto(0,0)
        score_red += 1
        pen.clear()
        pen.write("Red: {}  Blue : {}".format(score_red, score_blue),align="center", font=("Courier",24, "normal"))
        
        time.sleep(2)
    elif ball.xcor() <=-400:
        ball.goto(0,0)
        score_blue += 1
        pen._clear()
        pen.write("Red: {}  Blue : {}".format(score_red, score_blue),align="center", font=("Courier",24, "normal"))

        time.sleep(2)

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor()<=brick_right.ycor()+40 and ball.ycor()>=brick_right.ycor()-40 ):
        ball.dx *= -1
    elif (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor()<=brick_left.ycor()+40 and ball.ycor()>=brick_left.ycor()-40 ):
        ball.dx *= -1
      
    
    ball.setx(ball.dx + ball.xcor())
    ball.sety(ball.dy+ ball.ycor())
