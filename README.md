# Pong Game 🎮

This is a simple implementation of the classic Pong game built with Python and the `turtle` module. The game features two paddles, a bouncing ball, and a scoreboard to track points.

## Features

- Two-player functionality:
  - Player 1 controls the left paddle using `W` (up) and `S` (down).
  - Player 2 controls the right paddle using the `Up` and `Down` arrow keys.
- A ball that bounces off walls and paddles.
- A dynamic scoreboard to keep track of points.
- Adjustable ball speed for increasing difficulty.

---
Python Concepts Applied 🐍
Python programming concepts to implement the game logic and functionality:
1. Object-Oriented Programming (OOP)

    The game uses classes to encapsulate logic:
        Padlle represents the paddles with methods for movement.
        Ball handles the ball's behavior, including movement and collisions.
        Scoreboard manages the game's scoring system and updates the display.
    Inheritance is used in the Ball class by extending the functionality of the Turtle class from the turtle module.

2. Modules and Imports

    The project is modularized:
        padlle.py: Handles paddle functionality.
        ball.py: Contains logic for the ball.
        scoreboard.py: Manages scoring and updates.
    These modules are imported and used in the main game loop (main.py).

3. Event-Driven Programming

    The game listens to user input using screen.listen() and binds keys to paddle movement functions with screen.onkey().

4. Animation and Graphics

    The turtle module is used to create graphical elements like the paddles, ball, and scoreboard.
    Smooth animations are achieved by controlling the game loop with time.sleep() and screen.update().

5. Control Flow

    Conditional statements are used to detect collisions and scoring events.
    A while loop keeps the game running until the player exits.

6. Math and Coordinate Systems

    The game's logic uses basic math for collision detection and bouncing behavior.
    The xcor() and ycor() methods of Turtle are used to track object positions.

7. Custom Attributes and Methods

    Each class defines custom attributes and methods to encapsulate the game's logic:
        Example: ball.bounce_x() and ball.bounce_y() for reversing directions on collisions.
        The scoreboard updates the scores dynamically.
