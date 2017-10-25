import turtle

def drawshu(stx,sty,long):
    turtle.penup()
    turtle.goto(stx,sty)
    turtle.pendown()
    turtle.seth(-90)
    turtle.fd(long)

def drawheng(stx,sty,long):
    turtle.penup()
    turtle.goto(stx,sty)
    turtle.pendown()
    turtle.seth(0)
    turtle.fd(long)

def draw0(stx,sty,long):
    drawheng(stx,sty,long)
    drawheng(stx,sty - 2 * long, long)
    drawshu(stx,sty,2*long)
    drawshu(stx+long,sty,2*long)

def draw1(stx,sty,long):
    drawshu(stx,sty,2*long)

def draw2(stx,sty,long):
    drawheng(stx,sty,long)
    drawheng(stx,sty-long,long)
    drawheng(stx,sty-2*long,long)
    drawshu(stx+long,sty,long)
    drawshu(stx,sty-long,long)

def draw3(stx,sty,long):
    drawheng(stx,sty,long)
    drawheng(stx,sty-ong,long)
    drawheng(stx,sty-2*long,long)
    drawshu(stx+long,sty,2*long)

def draw4(stx,sty,long):
    drawheng(stx,sty-long,long)
    drawshu(stx,sty,long)
    drawshu(stx+long,sty,2*long)

def draw5(stx,sty,long):
    drawheng(stx,sty,long)
    drawheng(stx,sty-long,long)
    drawheng(stx,sty-2*long,long)
    drawshu(stx,sty,long)
    drawshu(stx+long,sty-long,long)
    
def draw6(stx,sty,long):
    drawheng(stx,sty,long)
    drawheng(stx,sty-long,long)
    drawheng(stx,sty-2*long,long)
    drawshu(stx,sty,2*long)
    drawshu(stx+long,sty-long,long)

def draw7(stx,sty,long):
    drawheng(stx,sty,long)
    drawshu(stx+long,sty,2*long)

def draw8(stx,sty,long):
    drawheng(stx,sty,long)
    drawheng(stx,sty-long,long)
    drawheng(stx,sty-2*long,long)
    drawshu(stx,sty,2*long)
    drawshu(stx+long,sty,2*long)

def draw9(stx,sty,long):
    drawheng(stx,sty,long)
    drawheng(stx,sty-long,long)
    drawshu(stx,sty,long)
    drawshu(stx+long,sty,2*long)

def drawpoint(stx,sty,size):
    turtle.penup()
    turtle.goto(stx,sty)
    turtle.shape()
    
def main():
    turtle.setup(1300,800,0,0)
    turtle.pensize(5)
    turtle.pencolor("red")
    #draw5(0,0,20)
    turtle.penup()
    stx = -300
    sty = 200
    long = 20
    draw2(stx,sty,long)
    stx += long + 10
    draw0(stx,sty,long)
    stx += long + 10
    draw1(stx,sty,long)
    stx += long + 10
    draw7(stx,sty,long)



main()
