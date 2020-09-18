import turtle
import time
import random
import winsound

delay = 0.1#snake1 speed
score = 0
high_score = 0

#Screen Setup
wn = turtle.Screen()
wn.title("Snake Game by Chris")
wn.bgcolor("black")#color of screen
wn.setup(width=600, height=600)#size of screen
wn.tracer(0)#turns off screen updates

#Borders
TopB = turtle.Turtle()
TopB.penup()
TopB.shape("square")
TopB.color("blue")
TopB.goto(0,250)
TopB.shapesize(stretch_wid=1, stretch_len = 30)
BottomB = turtle.Turtle()
BottomB.penup()
BottomB.shape("square")
BottomB.color("blue")
BottomB.goto(0,-280)
BottomB.shapesize(stretch_wid=1, stretch_len = 30)
LeftB = turtle.Turtle()
LeftB.penup()
LeftB.shape("square")
LeftB.color("blue")
LeftB.goto(-290,-20)
LeftB.shapesize(stretch_wid=27, stretch_len = 1)
RightB = turtle.Turtle()
RightB.penup()
RightB.shape("square")
RightB.color("blue")
RightB.goto(290,-20)
RightB.shapesize(stretch_wid=27, stretch_len = 1)

#Snake Head
head = turtle.Turtle()
head.speed #animation speed, 0 is the fastest
head.shape("circle")
head.color("green")
head.penup() #takes away the line that follows
head.goto(0,0)
head.direction = "stop"

#Apples
food = turtle.Turtle()
food.speed #animation speed, 0 is the fastest
food.shape("circle")
food.color("red")
food.penup() #takes away the line that follows
food.goto(0,100)

#Snake Body list
segments = []

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)#location of pen.write
pen.write("Score : {} High Score : {}".format(score, high_score), align="center", font=("Normal", 24, "underline"))

#Functions
def go_up():
    if head.direction != "down":#if head direction is not down
        head.direction = "up"#go up
def go_down():
    if head.direction != "up":#cant go up if going down
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"

#Movement by 20
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)#moves 20 pixels up
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#Keyboard Bindings
wn.listen()
wn.onkeypress(go_up, "Up")#move up
wn.onkeypress(go_down, "Down")#move down
wn.onkeypress(go_left, "Left")# move left
wn.onkeypress(go_right, "Right")# move right

#Main Game Loop
while True:
    wn.update()

    #Check for border collsions
    if head.xcor()>260 or head.xcor()<-260 or head.ycor()>220 or head.ycor()<-260:
        time.sleep(1)#pauses game with collsion
        head.goto(0,0)
        head.direction = "stop"

        #sound
        winsound.PlaySound("gameover.wav",winsound.SND_ASYNC)

        for segment in segments:
            segment.goto(1000,1000)#sends body off screen

        segments.clear()#clear body if collision
    
        score = 0#resets score when snake hits border
        pen.clear()
        pen.write("Score : {} High Score : {}".format(score, high_score), align="center", font=("Normal", 24, "underline"))

        #Reset snake speed
        delay = 0.1

    #Check for food collisons
    if head.distance(food)<20:#if collision
        food.goto(random.randrange(-260,260,20), random.randrange(-260,240,20))#Move apple randomly
        #x = random.randrange(-280,280,20)
        #y = random.randrange(-280,280,20)
        #food.goto(x,y)
        
        new_segment = turtle.Turtle()#add segment
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        #Sound
        winsound.PlaySound("appleeat.wav",winsound.SND_ASYNC)

        #Shorten Delay
        delay -=0.001#increases spped of snake with each apple collision

        #Scoring
        score += 10#10 for every apple
        if score > high_score:
            high_score = score#highest score becomes high score
        pen.clear()
        pen.write("Score : {} High Score : {}".format(score, high_score), align="center", font=("Normal", 24, "underline"))

    #Add segments to body in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    #Move 1st segment to head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    #Check if head hits body
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)#pauses game with collsion
            head.goto(0,0)
            head.direction = "stop"

            #sound
            winsound.PlaySound("gameover.wav",winsound.SND_ASYNC)

            score = 0#score resets with body collsion
            pen.clear()
            pen.write("Score : {} High Score : {}".format(score, high_score), align="center", font=("Normal", 24, "underline"))

            for segment in segments:#every body square in body
                segment.goto(1000,1000)#sends body off screen

            segments.clear#clears body

    time.sleep(delay)

wn.mainloop()

