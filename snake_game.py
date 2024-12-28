#Snake Game
#Author: Delaksan Sritharan
#Date: 18/12/2024

import turtle
import time
import random

delay = 0.1

#Score
score = 0
high_score = 0


#set up the screen
wn= turtle.Screen()
wn.title("Snake Game by @DelaksanSritharan") #title of the window
wn.bgcolor("green2") #background colour
wn.setup(width=600, height=600) #window size
wn.tracer(0) #Turns off screen updates

#Snake head

head = turtle.Turtle()
head.speed(0) #animation speed
head.shape("square")
head.color("blue")
head.penup() #It does not draw anything
head.goto(0,0) #starts center of the screen
head.direction = "stop"

#Snake food
food = turtle.Turtle()
food.speed(0) #animation speed
food.shape("circle")
food.color("red")
food.penup() #It does not draw anything
food.goto(0,100) #starts center of the screen

segments = []

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0  High Score: 0",align="center",font=("Courier",20,"normal"))

#Function
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"
    
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor() #can combine that into one line rather than two line
        head.setx(x + 20)
        # head.sety(head.xcor() + 20)

#Keyboard bindings
wn.listen() #asking to listen to clicks of the keys
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_right,"Right")
wn.onkeypress(go_left,"Left")



#Main game loop
while True:
    wn.update()

    #Check for a collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

    # Check for a collision with the food
    if head.distance(food) < 20:
        #Move the food to random spot
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x, y)
        
        # Add a segment
        new_segments = turtle.Turtle()
        new_segments.speed(0)
        new_segments.shape("square")
        new_segments.color("SteelBlue1")
        new_segments.penup()
        segments.append(new_segments)

        #Shorten the delay

        delay -= 0.001

        #Increase the score
        score += 10
        
        if score > high_score:
            high_score = score

        #
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score,high_score),align="center",font=("Courier",20,"normal"))

    #Move the end segment first in reverse order
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x ,y)

    #Move segement 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x , y)

    move()

    #Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            #Hide the segements
            for segment in segments:
                segment.goto(1000,1000)
            
            #Clear the segement list
            segments.clear()

            #Reset the score
            score = 0

            #Reset the delay
            delay = 0.1

            #Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score,high_score),align="center",font=("Courier",20,"normal"))

                
    time.sleep(delay)








wn.mainloop()