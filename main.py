from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Make Your Bet", prompt="red, blue, purple, green and yellow are racing,\nWho will "
                                                          "win?").lower()

gap = 360 / len(colors)
print(gap)
y_pos = -140

all_turtles = []
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos)
    y_pos += gap
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 225:
            is_race_on = False
            if user_bet == turtle.pencolor():
                screen.textinput(title="Congratulations", prompt="Your Turtle Won!!!")
            else:
                screen.textinput(title="Sorry", prompt=f"Your Turtle Lost!!! {turtle.pencolor()} Turtle Won.")
        else:
            turtle_steps = random.randint(0, 10)
            turtle.forward(turtle_steps)


screen.exitonclick()
