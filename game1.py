import turtle

# # Set up the screen
# screen = turtle.Screen()
# screen.title("Turtle Drawing Game")
# screen.bgcolor("white")
# screen.setup(width=800, height=600)

# Create the turtle
brush = turtle.Turtle()
#drawing_turtle.shape("turtle")
#brush.color("black")

# Function to move the turtle forward
def move_forward():
    brush.forward(10)

# Function to move the turtle backward
def move_backward():
    brush.backward(10)

# Function to turn the turtle left
def turn_left():
    brush.left(15)

# Function to turn the turtle right
def turn_right():
    brush.right(15)

# Function to change the pen color to red
def change_color_red():
   brush.color("red")

# Function to change the pen color to blue
def change_color_blue():
    brush.color("blue")

# Function to change the pen color to green
def green():
    brush.color("green")

# Function to lift the pen up (stop drawing)
def pen_up():
    brush.penup()

# Function to put the pen down (start drawing)
def pen_down():
    brush.pendown()
def clear():
    brush.clear()

# Keyboard bindings
turtle.listen()
turtle.onkeypress(move_forward, "Up")
turtle.onkeypress(move_backward, "Down")
turtle.onkeypress(turn_left, "Left")
turtle.onkeypress(turn_right, "Right")
turtle.onkeypress(change_color_red, "r")
turtle.onkeypress(change_color_blue, "b")
turtle.onkeypress(green, "g")
turtle.onkeypress(pen_up, "u")
turtle.onkeypress(pen_down, "d")
turtle.onkeypress(clear, "c")


turtle.done()
