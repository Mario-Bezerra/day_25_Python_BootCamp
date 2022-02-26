import turtle
import pandas
import state_right

# creating screen
screen = turtle.Screen()
screen.title("U.S.A Guess Game")
# adding the image in the turtle class
image = "blank_states_img.gif"
screen.addshape(image)
# turning the shape form to the image
turtle.shape(image)

right_states = []
right_count = 0
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()


while right_count < 50:
    guess = str(screen.textinput(title=f" {right_count}/50 U.S Game",
                                 prompt="Guess a state")).title()
    # making a list with the states that don't were marked
    if guess == "Exit":
        states_to_learn = [states for states in all_states if states not in right_states]
        new_df = pandas.DataFrame(states_to_learn)
        new_df.to_csv("missing_states_list.csv")
        break
    pen = turtle.Turtle()
    pen.penup()
    pen.hideturtle()
    # checking the answer and creating the list of right guessing
    if guess in all_states and guess not in right_states:
        state_datas = data[data.state == guess]
        pen.goto(int(state_datas.x), int(state_datas.y))
        pen.write(f"{guess}", align="center", font=["Arial", 8])
        right_count += 1
        right_states.append(guess)

