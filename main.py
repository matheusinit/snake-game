import sys, pygame, random
from typing import Tuple
from snake import Snake
from fruit import Fruit
from utils import Utils
from colors import BLACK, RED, GREEN

pygame.init()

# Set a tuple of width as 800 and height as 600
size = width, height = 800, 600

# Pixel with 20 as size
pixel: int = 20

# Start points as 0
points: int = 0

# Last position
last_pos: Tuple[int, int] = (0, 0)

# Scren set to the size
screen = pygame.display.set_mode(size)

# X and Y of the snake
x, y = 0, 0
snake_body = [(0, 0)]

fruit_x, fruit_y = 5, 10

snake = Snake(GREEN, pixel, screen)
fruit = Fruit(RED, pixel, screen)
utils = Utils()

"""
| Keep running forever
"""
while True:
    """
    | Keep listening for events to react to it
    | In case of a Key Right, goes right
    | In case of a Key Left, goes left
    | In case of a Key Up, goes up 
    | In case of a Key Down, goes down
    """
    for event in pygame.event.get():
        """
        | Closes when click at X button
        """
        if event.type == pygame.QUIT: 
            sys.exit()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                x += 1
            elif event.key == pygame.K_DOWN:
                y += 1
            elif event.key == pygame.K_LEFT:
                x -= 1
            elif event.key == pygame.K_UP:
                y -= 1
                
            # Makes the snake move with X and Y updated
            snake.move((x, y))
    """
    | When snake catch the fruit, increases by one the points, increases snake and generate new position for fruit
    """
    if x == fruit_x and y == fruit_y:
        points += 1

        fruit_x = utils.generate_position(0, width // pixel - 1)
        fruit_y = utils.generate_position(0, height // pixel - 1)

        if x != last_pos[0]:
            snake.increase_body()

        elif y != last_pos[1]:
            snake.increase_body()


    # Fill the background as black
    screen.fill(BLACK)

    """
    | If snake pass the right border, goes to the left border
    """
    if x >= width // pixel:
        # Redefine X
        x = (snake.body[0][0] * pixel) % width
        snake.update_head((x, y))

    """
    | If snake pass the left border, goes to the right border
    """
    if x < 0:
        x = width // pixel - 1
        snake.update_head((x, y))

    """
    | If snake pass the top border, goes to the bottom border
    """
    if y < 0:
        y = height // pixel - 1 
        snake.update_head((x, y))

    """
    | If snake pass the bottom border, goes to the top border
    """
    if y >= height // pixel:
        y = (snake.body[0][1] * pixel) % height
        snake.update_head((x, y))

    """
    | Print at console when used flag debug
    """
    if len(sys.argv) > 1 and sys.argv[1] == '--debug':
        # Draw snake
        print(last_pos)
        print(snake.body)
        print(f"Pontos: {points}")

    # Draw snake
    snake.draw()

    # Draw fruit
    fruit.draw((fruit_x, fruit_y))

    pygame.display.flip()

