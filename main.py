import turtle
from turtle import Turtle
import pandas as pd

screen = turtle.Screen()

turtle = Turtle()

data = pd.read_csv("50_states.csv")

screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
answers_given = []

while len(answers_given) < 50:
    answer_state = screen.textinput(title = "Guess The State Game", prompt = "Whats another state's name?")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        break

    answers_given.append(answer_state)
    # Create List of states in the .csv fil
    list_of_states = data["state"].to_list()

    # Check to see if state is in our list of states.
    if answer_state in list_of_states:

        state_xy = data[data["state"] == answer_state]
        x = int(state_xy.x)
        y = int(state_xy.y)
        scoreboard = Turtle()
        scoreboard.penup()
        scoreboard.hideturtle()
        scoreboard.goto(x, y)

        scoreboard.write(answer_state, align="center", font=("Currior", 10, "normal"))

    else:
        print("you suck")

#states_to_learn = []

#for a in list_of_states:
#    if a not in answers_given:
#        states_to_learn.append(a)
states_to_learn = [state for state in list_of_states if state not in answers_given]

states_to_learn_df = pd.DataFrame(states_to_learn)

states_to_learn_df.to_csv("data_out.csv")
5

