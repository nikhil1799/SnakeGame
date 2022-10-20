import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
score = 0

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_status = True
while game_status:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 17:
        food.hit()
        snake.extend()
        score += 1
        scoreboard.clear()
        scoreboard.write(f'Score: {score}', move=False, align='center', font=('Courier', 17, 'bold'))
    if snake.head.xcor() > 299 or snake.head.xcor() < -300 or snake.head.ycor() > 280 or snake.head.ycor() < -299:
        game_status = False
        scoreboard.clear()
        scoreboard.write(f'Game Over. Score: {score}', move=False, align='center', font=('Courier', 17, 'bold'))

    for segment in snake.squares[1:]:

        if snake.head.distance(segment) < 10:
            game_status = False
            scoreboard.clear()
            scoreboard.write(f'Game Over. Score: {score}', move=False, align='center', font=('Courier', 17, 'bold'))




screen.exitonclick()
