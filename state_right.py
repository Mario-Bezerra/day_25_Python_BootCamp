from turtle import Turtle
from main import name_state , x_state , y_state

class RightAnswer(Turtle):
    def __init__(self, x_state, y_state, name_state):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto((x_state, y_state))
        self.write(f"{name_state}", False, align="center", font=("Arial", 12, "normal"))
