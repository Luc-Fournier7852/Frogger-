from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.Level =1
        self.highscore = 0

    def draw_screen(self):
        self.goto(-250,260)
        self.write("Level:", align='center', font=FONT)

    def welcome_msg(self):
        self.goto(0, 0)
        self.write("Welcome to Crossy Road!", align='center', font=("Courier", 25, "normal"))

    def level(self):
        self.goto(-190, 260)
        self.write(self.Level, align='center', font=FONT)
    def increase_level(self):


        self.Level +=1
        if self.Level>self.highscore:
            self.highscore = self.Level
            with open("highscore.txt", mode="w") as file:
                file.write(str(self.highscore))
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", align='center', font=FONT)
    def high_score(self):
        with open("highscore.txt") as file:
            contents = file.read()
            self.goto(180, 260)
            self.write(f"Highscore: {contents}", align='center', font=FONT)
    pass
