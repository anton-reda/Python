import turtle

wind = turtle.Screen() #intialization of the screen 
wind.title("ping pong game ") #setting the title of the window 
wind.bgcolor("black")  #setting the background_color of the screen
wind.setup(width= 800 , height=600) # setting width and height of the screen
wind.tracer(0)  # stops the window from updating automatically


# Madrab 1
madrab1 = turtle.Turtle()   # intializes turtle object (shape)
madrab1.speed(0)            # set the speed of the animation to the highest
madrab1.shape("square")     # set the shape of the object 
madrab1.shapesize(stretch_wid=5, stretch_len=1)     # stretches the shape to meet the size 
madrab1.color("blue")       # set the color of the shape 
madrab1.penup()             # stops the object from drawing lines
madrab1.goto(-350,0)        # set the position of the object 

# Mabrab 2
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.shapesize(stretch_wid=5, stretch_len=1)
madrab2.color("red")
madrab2.penup()
madrab2.goto(350,0)

# Ball 
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.1
ball.dy = 0.1

# Score  
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player 1 : 0    Player 2 : 0", align="center", font=("Courier", 24 ,"normal"))




# functions of Madrab 1
def madrab1_up():
    y = madrab1.ycor()  # get y coordinate of madrab 1
    y += 20             # increment y coordinate by 20 
    madrab1.sety(y)     # setting y of madrab 1 to the ney y coordinate 

def madrab1_down():
    y = madrab1.ycor()  
    y -= 20             # decrement y coordinate by 20 
    madrab1.sety(y)

# keyboard bindings
wind.listen()                       # tell the window to expect input from the keyboard 
wind.onkeypress(madrab1_up , "w")   # when pressing w key the function madrab1_up is called 
wind.onkeypress(madrab1_down , "s")


# functions of Madrab 2
def madrab2_up():
    y = madrab2.ycor()  
    y += 20
    madrab2.sety(y)

def madrab2_down():
    y = madrab2.ycor()  
    y -= 20
    madrab2.sety(y)    

# keyboard bindings
wind.onkeypress(madrab2_up , "Up")  # when pressing UP arrow key the function madrab1_up is called 
wind.onkeypress(madrab2_down , "Down")

# setting esc button to exit the game 
def exit_game():
    wind.bye()
wind.onkeypress(exit_game,"Escape ")  


#main game loop
while True: 
    wind.update()  # updates the screen every time the games runs

    # moving the ball
    ball.setx(ball.xcor() + ball.dx)   # ball starts at 0  and everytime loops runs --> +0.2 to x-axis
    ball.sety(ball.ycor() + ball.dy)   # ball starts at 0  and everytime loops runs --> +0.2 to y-axis


    # border check  , top border 300px , bottom border -300px , ball is 20px
    if ball.ycor() > 290 : # if ball is at top border 
        ball.sety(290)     # set y coordinate to 290
        ball.dy *= -1      # reverse ball direction making dy = -0.3
    
    if ball.ycor() < -290 :
        ball.sety(-290)
        ball.dy *= -1



    # Madrab  1 collision with upper and lower walls
    if  madrab1.ycor() > 250 :
        madrab1.sety(245)
    
    if  madrab1.ycor() < -250 :
        madrab1.sety(-240)

    # Madrab  2 collision with upper and lower walls
    if  madrab2.ycor() > 250 :
        madrab2.sety(245)
    
    if  madrab2.ycor() < -250 :
        madrab2.sety(-240)



    # ball collision with the two sides 
    if ball.xcor() > 390 : # if ball is at right border 
        ball.goto(0,0)     # return ball to center 
        ball.dx *= -1      # reverse the x direction
        score1 += 1  
        score.clear()
        score.write("Player 1 : {}    Player 2 : {}".format(score1,score2), align="center", font=("Courier", 24 ,"normal"))

    if ball.xcor() < -390 :
       ball.goto(0,0)
       ball.dx *= -1
       score2 += 1  
       score.clear()
       score.write("Player 1 : {}    Player 2 : {}".format(score1,score2), align="center", font=("Courier", 24 ,"normal"))



    # Madrab and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and ball.ycor() < madrab2.ycor() + 40 and ball.ycor() > madrab2.ycor() - 40:
        ball.setx(340)
        ball.dx *= -1
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and ball.ycor() < madrab1.ycor() + 40 and ball.ycor() > madrab1.ycor() - 40:
        ball.setx(-340)
        ball.dx *= -1




    if score1 == 10 or score2 == 10:
        # Hiding the paddles and ball
        madrab1.hideturtle()
        madrab2.hideturtle()
        ball.hideturtle()
        if score1 == 10 :
        # Displaying "Game Over"
            game_over = turtle.Turtle()  
            game_over.speed(0)
            game_over.color("white")
            game_over.penup()
            game_over.hideturtle()
            game_over.goto(0, 0)
            game_over.write("Game Over\n", align="center", font=("Courier", 50, "bold"))
            game_over.write("Player 1 Wins !", align="center", font=("Courier", 30, "normal"))
        else:
            game_over = turtle.Turtle()  
            game_over.speed(0)
            game_over.color("white")
            game_over.hideturtle()
            game_over.goto(0, 0)
            game_over.write("Game Over\n", align="center", font=("Courier", 50, "bold"))
            game_over.write("Player 2 Wins !", align="center", font=("Courier", 30, "normal"))
        
        
        

        