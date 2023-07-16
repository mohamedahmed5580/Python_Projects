import turtle

wind=turtle.Screen()
wind.title("ping pong game")
wind.bgcolor("black")
wind.setup(width=1000,height=600)
wind.tracer(0)

#madrab1
madrab1=turtle.Turtle()
madrab1.speed(0)
madrab1.shape("square")
madrab1.color("blue")
madrab1.shapesize(stretch_wid=5,stretch_len=1)
madrab1.penup()
madrab1.goto(-360,0)

#madrab2
madrab2=turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red")
madrab2.shapesize(stretch_wid=5,stretch_len=1)
madrab2.penup()
madrab2.goto(360,0)

#boll
boll=turtle.Turtle()
boll.speed(0)
boll.shape("circle")
boll.color("white")

boll.penup()
boll.goto(0,0)
bolldx =0.4
bolldy =0.4

def madrab_up():
    y=madrab1.ycor()
    y+=20
    madrab1.sety(y)

def madrab_button():

    x=madrab1.ycor()
    x+=-20
    madrab1.sety(x)

def madrab_up2():
    y=madrab2.ycor()
    y+=20
    madrab2.sety(y)

def madrab_dwon2():
    y=madrab2.ycor()
    y+=-20
    madrab2.sety(y)

wind.listen()
wind.onkeypress (madrab_up, "w" )
wind.onkeypress (madrab_button, "s" )
wind.onkeypress (madrab_up2, "Up" )
wind.onkeypress (madrab_dwon2, "Down" )

while True:
    wind.update()

    boll.setx(boll.xcor() + bolldx)
    boll.sety(boll.ycor() + bolldy)

    if boll.ycor() > 290:
        boll.sety(290)
        bolldy *=-1


    if boll.ycor() <-290:
        boll.sety(-290)
        bolldy *=-1

    if boll.xcor() > 390:
        boll.goto(0,0)
        bolldx *=-1


    if boll.xcor() <-390:
        boll.goto(0,0)
        bolldx *=-1

    if (boll.xcor() > 340 and boll.xcor() < 350 and (boll.ycor() < madrab2.ycor() + 40 and boll.ycor() > madrab2.ycor() -40)):
        boll.setx(340)
        bolldx *=-1
    
    if (boll.xcor() < -340 and boll.xcor() >  -350 and (boll.ycor() < madrab1.ycor() + 40 and boll.ycor() > madrab1.ycor() -40)):
        boll.setx(-340)
        bolldx *=-1
    