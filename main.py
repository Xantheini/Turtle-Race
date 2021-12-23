from turtle import Turtle, Screen
import random
import heroes

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
names = []
all_turtles = []

# Give turtles hero names 
for _ in range(6):
    names.append(heroes.gen())

ycor_up = 0

for x in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-125 + ycor_up)
    new_turtle.color(colors[x])
    new_turtle.speed(10)
    all_turtles.append(new_turtle)
    ycor_up += 50

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            color_index = colors.index(winning_color)
            winning_name = names[color_index]
            if winning_color == user_bet.lower():
                print(f"You've won! {winning_name}, the {winning_color} turtle, is the winner!")
            else:
                print(f"You've lost! {winning_name}, the {winning_color} turtle, is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
