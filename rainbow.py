import turtle
colors=["red","purple","green","orange","blue",]
t = turtle.Pen()
turtle.bgcolor("black")
def fun():
   for i in range(360):
     t.pencolor(colors[i%5])
     t.width(i//100+1)
     t.forward(i)
     t.left(59)
     t.speed(100)
        

fun()
turtle.done()     