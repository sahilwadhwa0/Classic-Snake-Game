from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode='r') as file:
            self.content = int(file.read())

        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_score_board()

    def refresh_score(self):
        self.score += 1
        self.update_score_board()

    def reset(self):
        if self.content < self.score:
            self.content = self.score
            with open("data.txt", mode='w') as file:
                file.write(str(self.score))
        self.score = 0
        self.update_score_board()

    # def game_over(self):
    #
    #     self.hideturtle()
    #     self.penup()
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def update_score_board(self):
        self.clear()
        self.write(arg=f"score : {self.score}    high score :{self.content}", align=ALIGNMENT, font=FONT)
