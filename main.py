import turtle
import pandas

screen = turtle.Screen()
turt = turtle.Turtle()
turt.hideturtle()
turt.penup()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")

correct = 0
game_is_on = True

correct_guesses = []
new_data_list = []

while game_is_on:
    answer_state = screen.textinput(title=f"{correct}/50 states correct", prompt="Enter the name of the state")
    capital_answer = answer_state.title()
    data_list = data["state"].to_list()

    if capital_answer in data_list and capital_answer not in correct_guesses:
        x_cor = data.loc[data_list.index(capital_answer), "x"]
        y_cor = data.loc[data_list.index(capital_answer), "y"]
        turt.goto(x_cor, y_cor)
        turt.write(capital_answer)
        correct += 1
        if capital_answer not in correct_guesses:
            correct_guesses.append(capital_answer)

    if correct == 50 or capital_answer == "Exit":
        game_is_on = False

for state in data_list:
    if state not in correct_guesses:
        new_data_list.append(state)


new_dataframe = pandas.DataFrame(new_data_list)
new_data = new_dataframe.to_csv("states_missed.csv")



