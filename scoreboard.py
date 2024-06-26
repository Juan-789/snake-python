from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 250)
        self.color('white')
        self.hideturtle()
        self.penup()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f'Score: {self.score}', False,
                   'center', ('Arial', 15, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', False, 'center', ('Courier', 24, 'normal'))

