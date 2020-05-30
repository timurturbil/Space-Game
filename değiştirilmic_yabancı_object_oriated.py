import turtle
import random
import math

wn = turtle.Screen()
wn.bgcolor("white")
wn.title("simple python project")
wn.bgpic("space_invaders_background.gif")  # tkinter kütüphanesini yükle
turtle.register_shape("invader.gif")



class oyun(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("blue")
        self.goto(-290,310)
        self.score = 0
    def update_score(self):
        self.clear()
        self.write("Score : {}".format(self.score), False , align="left", font=("Arial", 14,"normal"))
    def change_score(self, points):
        self.score += points
        self.update_score()
"""     def play_sound(self, filename):    #tkinter kütüphanesi lazım
        os.system("afplay {}&".format(filename)) """
class mermi(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.color("yellow")
        self.shape("circle")
        
        self.shapesize(0.5,0.5)
        self.speed = 10
        self.goto(x=0,y=-200)   
    def move(self):
        self.forward(self.speed) 
    def atış(self):
        self.setheading(timur.heading())
        if self.ycor() < 310 or self.ycor() > 310:
            self.forward(5)
            x = timur.xcor()
            y = timur.ycor()
            bullet.setposition(x, y)

class Border(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.color("black")
        self.pensize(5)
    def draw_border(self):
        self.penup()
        self.goto(-900,-900)
        self.pendown()
        self.goto(-900,900)
        self.goto(900,900)
        self.goto(900,-900) 
        self.goto(-900,-900)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("triangle")
        self.color("blue")
        self.speed = 1
        self.goto(x=0,y=-200)

    def move(self):
        self.forward(self.speed) 
        if self.xcor() < -300 or self.xcor() > 300:
            self.left(90)
        elif self.ycor() < -300 or self.ycor() > 300:
            self.left(90)
    def turnleft(self):
        self.left(30)
    def turnright(self):
        self.right(30) 
    def increasingspeed(self):
        self.speed += 1 
    def decreasingspeed(self):
        self.speed -= 1    
    


class bocekler(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed = 0.3
        self.color("red")
        self.shape("invader.gif")
        self.goto(random.randint(-200,200), random.randint(150,250))
    def jump(self):
        self.goto(290,250)
    def move(self):
        self.forward(self.speed) 
        
        if self.xcor() < -300 or self.xcor() > 300:
            for i in bocek:
                y = i.ycor()
                y -= 40
                i.sety(y)
                i.left(180)
        elif self.ycor() > 250:
            self.left(90)

 
    
"""     def hız_arttır(self):
        self.speed += 5  """       
def vurdumu(t1,t2):
    a = t1.xcor() - t2.xcor()
    b = t1.ycor() - t2.ycor()
    distance = math.sqrt((a**2) + (b**2))
    if distance < 20:
        return True
    else:
        return False    

timur = Player()
border = Border()
kısım = oyun()
bullet = mermi()
bocek = []
for count in range(10):
    bocek.append(bocekler())


border.draw_border()
turtle.onkey(timur.turnleft, "Left")
turtle.onkey(timur.turnright, "Right")
turtle.onkey(timur.increasingspeed, "Up")
turtle.onkey(timur.decreasingspeed, "Down")
turtle.onkey(bullet.atış, "space")
turtle.listen()

""" turtle.onkey(bullet, "1") """



wn.tracer(0)

while True:
    wn.update()
    timur.move() 
    bullet.move()
    
    for i in bocek:
        i.move()
        if vurdumu(bullet,i):
            i.jump()
            """ i.hız_arttır() """
            kısım.change_score(1)
            """ kısım.play_sound("collision.mp3") """  
