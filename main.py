import pandas
from turtle import Turtle, Screen

def init():
    data = pandas.read_csv("50_states.csv")

    IMAGE = "blank_states_img.gif"

    s = Screen()

    s.addshape(IMAGE)
    s.bgpic(IMAGE)

    t = Turtle()
    t.hideturtle()
    t.pu()
    main(s,t,data)

def main(s,t,data):
    guessed_states = []
    while len(guessed_states) < 50:
        user_input = s.textinput(title=f'{len(guessed_states)}/50 states',prompt="Enter a state name").title()
        #Query through state col for user input

        if user_input == "Exit":
            break
        state_row = data[data["state"] == user_input]

        if state_row.empty:
            pass
        else:
            guessed_states.append(user_input)
            t.goto(int(state_row.x),int(state_row.y))
            t.write(user_input)

    missing_states = []
    for state in data.state.to_list():
        if state not in guessed_states:
            missing_states.append(state)
    new_data = pandas.DataFrame(missing_states)
    new_data.to_csv("states_to_learn.csv")
    s.bye()

    s.exitonclick()


init()