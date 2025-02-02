import turtle

# Manually set screen size
screen = turtle.Screen()
screen.setup(width=800, height=800)  # Ensures it's not tiny
screen.setworldcoordinates(-400, -400, 400, 400)  # Centers the drawing area

# Create a turtle and make sure it's visible
pen = turtle.Turtle()
pen.speed(1)  # Slow it down so we can see movement
pen.penup()
pen.goto(-50, 50)  # Move to a visible location
pen.pendown()
pen.forward(100)  # Draw a line

# Keep window open
turtle.done()
