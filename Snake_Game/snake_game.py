import pygame
import time
import random

pygame.init()

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set up display
width, height = 800, 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Set up clock
clock = pygame.time.Clock()

# Set up snake and food
snake_block = 10
snake_speed = 15
font = pygame.font.SysFont(None, 35)

# Function to draw the snake
def draw_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(display, green, [block[0], block[1], snake_block, snake_block])

# Function to display the score
def Your_score(score):
    value = font.render("Your Score: " + str(score), True, white)
    display.blit(value, [0, 0])

# Main game loop
def gameLoop():
    #Initializing Game State Variables:
    game_over = False
    game_close = False
    
    #Initializing Snake and Food Positions:
    x1, y1 = width / 2, height / 2
    x1_change, y1_change = 0, 0

    #Initializing Snake List and Length:
    snake_list = []
    length_of_snake = 1

    #Initializing Food Position:
    foodx, foody = round(random.randrange(0, width - snake_block) / 10.0) * 10.0, round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    #Outer Game Loop:
    while not game_over:
        #Inner Game Loop for Game Over Screen:
        while game_close:
            display.fill(black)
            message = font.render("You Lost! Press C-Play Again or Q-Quit", True, red)
            display.blit(message, [width / 6, height / 3])
            Your_score(length_of_snake - 1)
            pygame.display.update()
            
        #Handling Events Outside the Inner Loop:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        gameLoop()
                        
        #Handling Key Presses for Snake Movement:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        #Checking for Game Over Conditions:
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        #Updating Snake Position and Length:
        x1 += x1_change
        y1 += y1_change
        #Drawing Elements on the Screen:
        display.fill(black)
        pygame.draw.rect(display, blue, [foodx, foody, snake_block, snake_block])
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        Your_score(length_of_snake - 1)

        pygame.display.update()

        #Checking for Food Consumption:
        if x1 == foodx and y1 == foody:
            foodx, foody = round(random.randrange(0, width - snake_block) / 10.0) * 10.0, round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
            
        #Controlling Game Speed:
        clock.tick(snake_speed)
        
#Exiting the Game:
    pygame.quit()
    quit()
    
#Calling the Main Game Loop:
gameLoop()
