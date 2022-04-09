from turtle import Turtle
import random


class Food(Turtle):  # here we inherit turtle class to food class .

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # because we have to short the size of turtle .
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):

        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)
