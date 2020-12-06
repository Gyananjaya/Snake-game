import pygame
import random
import math
import os
pygame.init()
# colour
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
# creating window
screen_width = 800
screen_height = 600
gamewindow = pygame.display.set_mode((screen_width, screen_height))
#logo of game
icon = pygame.image.load('logo.png')
pygame.display.set_icon(icon)
# wellcome window background
wellcome_window = pygame.image.load("wellcome.jpg")
mainbg = pygame.image.load("mainbg.jpg")
gameover = pygame.image.load("gameover1.jpg")
wellcome_window = pygame.transform.scale(wellcome_window,(screen_width,screen_height)).convert_alpha()
mainbg = pygame.transform.scale(mainbg,(screen_width,screen_height)).convert_alpha()
gameover = pygame.transform.scale(gameover,(screen_width,screen_height)).convert_alpha()

# game titel
pygame.display.set_caption("snake world")
pygame.display.update()
# game specific variables

global game_over
clock = pygame.time.Clock()

# snake
def plot_snake(gamewindow, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(gamewindow, white, [x, y, snake_size, snake_size])


# collision
def collision(snake_x, snake_y, food_x, food_y):
    distance = math.sqrt((math.pow(snake_x - food_x, 2)) + (math.pow(snake_y - food_y, 2)))
    if distance < 27:
        return True
    else:
        return False


# score
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10
score = 0

def text_screen(text,color,x,y):
    screen_text = font.render(text,True,red,None)
    gamewindow.blit(screen_text,[x,y])

# game over
over_font = pygame.font.Font('freesansbold.ttf', 40)


def game_over_text():
    over_text = over_font.render("HIT SPACE BAR TO PLAY AGAIN", True, (255, 0, 255))
    gamewindow.blit(over_text, (50, 460))
# wellcome window
def welcome():
    exit_game = False
    while not exit_game:
        #gamewindow.fill(white)
        gamewindow.blit(wellcome_window,(0,0))
        text_screen("WELLCOME TO SNAKE WORLD",red,160,460)
        text_screen("( *****  Press K To Play The Game ***** )", red, 80, 540)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_k:
                    game_loop()

        pygame.display.update()
        clock.tick(50)

# game loop
def game_loop():
    exit_game = False
    game_over = True
    snake_x = 45
    snake_y = 55
    snake_size = 20
    snake_list = []
    snake_length = 1
    food_x = random.randint(40, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    food_size = 20
    velocity_x = 0
    velocity_y = 0
    fps = 40
    score = 0
    #HighScore = 0
    #to check if HighScore is present or not
    if (not os.path.exists("HighScore") ):
        with open("HighScore", "w")as f:
            f.write('0')
    # high score
    with open("HighScore", "r") as f:
        HighScore = f.read()

    while not exit_game:
        #gamewindow.fill((0, 0, 0))
        gamewindow.blit(mainbg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            # key up down features
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    velocity_x = +4
                    velocity_y = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    velocity_x = -4
                    velocity_y = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    velocity_y = -4
                    velocity_x = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    velocity_y = +4
                    velocity_x = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    welcome()

        snake_x += velocity_x
        snake_y += velocity_y

        # colision
        iscollision = collision(snake_x, snake_y, food_x, food_y)
        if iscollision:
            score += 10
            snake_length += 5
            #print("score:",score)
            food_x = random.randint(40, screen_width / 2)
            food_y = random.randint(20, screen_height / 2)
            if score > int(HighScore):
                HighScore = score
        #gamewindow.fill(white)
        # pygame.draw.rect(gamewindow,black,[snake_x,snake_y,snake_size,snake_size])
        pygame.draw.rect(gamewindow, red, [food_x, food_y, food_size, food_size])
        head = []
        head.append(snake_x)
        head.append(snake_y)
        snake_list.append(head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        if snake_x < 5 or snake_x > (screen_width - 5) or snake_y < 5 or snake_y > (screen_height - 5) and head in snake_list[:-1]:
            game_over = True
            #gamewindow.fill(white)
            gamewindow.blit(gameover, (0, 0))
            game_over_text()
            with open("HighScore","w") as f:
                f.write(str(HighScore))


        plot_snake(gamewindow, white, snake_list, snake_size)
        text_screen("Score :" + str(score)+ " HighScore:"+str(HighScore), red, 5, 5)

        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
welcome()
#game_loop()

