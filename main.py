# install pygame library and import it => pip install pygame
import pygame
import time
import random

# Initialize Pygame modules
pygame.init()

# Color Definition
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BlACK = (0,0,0)
WHITE = (255,255,255)

# Snake Dimension
snake_size = 10

# nabdou nasen3ou fi window
WIN_WIDTH = 500
WIN_HEIGHT = 400

clock = pygame.time.Clock()

def show_message(message,color):
    font = pygame.font.SysFont("arial",40)
    messsage_style= font.render(message,True,color)
    window.blit(messsage_style,(WIN_WIDTH/3,WIN_HEIGHT/3))

def draw_snake(snake_list):
    for t in snake_list:
        pygame.draw.rect(window,GREEN,[t[0],t[1],snake_size,snake_size])

def show_score(score,color):
    font_style = pygame.font.SysFont("verdana",25)
    score_style = font_style.render("Score: "+str(score),True,color)
    window.blit(score_style,(10,10))
    pygame.draw.line(window,color,(0,50),(WIN_WIDTH,50))

def game_loop():
    x = 250
    y = 200
    x_change = 0
    y_change = 0

    foodX = random.randrange(0,WIN_WIDTH,10)
    foodY = random.randrange(50,WIN_HEIGHT,10)

    snake_length = 1
    snake_list=[]


    game_close = False
    game_over = False
    while not game_close and not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x_change = 10
                    y_change = 0
                elif event.key == pygame.K_LEFT:
                    x_change = -10
                    y_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = 10
                    x_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -10
                    x_change = 0

        x += x_change
        y += y_change

        #condition of game over
        if x < 0 or x >=WIN_WIDTH or y < 50 or y >= WIN_HEIGHT:
            game_over = True
            show_message("Game Over",RED)
            pygame.display.update()
            time.sleep(5)
        else:
            #clear the screen
            window.fill(BlACK)
            pygame.draw.rect(window,BLUE,(foodX,foodY,10,10))
            # pygame.draw.rect(window,GREEN,(x,y,snake_size,snake_size))
            snake_head=(x,y)
            snake_list.append(snake_head)
            if len(snake_list) > snake_length:
                del snake_list[0]
            draw_snake(snake_list)
            show_score(snake_length-1,WHITE)
            pygame.display.update()
            clock.tick(10)

            for b in snake_list[:-1]:
                if b == snake_head:
                    game_over= True
                    show_message("Game Over", RED)
                    pygame.display.update()
                    time.sleep(5)

            if x == foodX and y== foodY:
                snake_length+=1
                foodX = random.randrange(0, WIN_WIDTH, 10)
                foodY = random.randrange(50, WIN_HEIGHT, 10)



window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Snake Game")
game_loop()
pygame.quit()


