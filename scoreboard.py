from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,280)
        self.hideturtle()
        self.color('white')
        self.write(f'Score:', move=False, align='center', font=('Courier', 17, 'bold'))



