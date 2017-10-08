import turtle

def drawWang(heng1, heng2, shu, stx, sty):
    turtle.seth(0)
    turtle.fd(heng1)
    turtle.penup()
    turtle.goto(stx + heng1/2 - heng2/2,sty -shu/2)
    turtle.seth(0)
    turtle.pendown()
    turtle.fd(heng2)
    turtle.penup()
    turtle.goto(stx + heng1/2,sty)
    turtle.pendown()
    turtle.seth(-90)
    turtle.fd(shu)
    turtle.penup()
    turtle.goto(stx,sty - shu)
    turtle.pendown()
    turtle.seth(0)
    turtle.fd(heng1)
    turtle.penup()
    

def main():
    turtle.setup(1300, 800, 0, 0)
    turtle.pensize(3)
    turtle.pencolor("black")
    turtle.speed(10)
    turtle.penup()
    stx = -300
    sty = 300
    turtle.goto(stx,sty)
    turtle.pendown()
    drawWang(300,200,200,stx, sty)
    


main()
