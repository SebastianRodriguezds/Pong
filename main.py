from turtle import Screen, Turtle
from padlle import Padlle
from ball import Ball
import time
from scoreboard import Scoreboard


DOWN = -10
UP = 10

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Padlle((350, 0))
l_paddle = Padlle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()







screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

speed = 0.1

game_is_on = True
while game_is_on:
  time.sleep(ball.move_speed)
  screen.update()
  ball.move()

  #Detect collision with wall
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()
  
 
  #Detect collision with paddles
  if ball.distance(r_paddle)  < 40 and ball.xcor() > 320 or ball.distance(l_paddle) < 40 and ball.xcor() < -320:
    ball.bounce_x()
    speed -= 0.005
  
  #Detect R misses
  if ball.xcor() > 390:
    ball.reset_position()
    scoreboard.l_point()
  
  #Detect R misses
  if ball.xcor() < -390:
    ball.reset_position()
    scoreboard.r_point()
  



screen.exitonclick()