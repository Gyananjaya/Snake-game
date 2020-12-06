import pygame
import random
import math
pygame.init()
#colour
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
#creating window
screen_width = 900
screen_height = 800
gamewindow = pygame.display.set_mode((screen_width,screen_height))
# game titel
pygame.display.set_caption("snake world")
pygame.display.update()
# game specific variables
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


clock = pygame.time.Clock()
# snake
def plot_snake(gamewindow,color,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gamewindow, black, [x,y, snake_size, snake_size])


# collision
def collision(snake_x, snake_y,food_x, food_y):
    distance = math.sqrt((math.pow(snake_x - food_x, 2)) + (math.pow(snake_y - food_y, 2)))
    if distance < 27:
        return True
    else:
        return False
# score
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10
score_value = 0
def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (255, 0, 255))
    gamewindow.blit(score, (x, y))

# game over
over_font = pygame.font.Font('freesansbold.ttf', 60)
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 0, 255))
    gamewindow.blit(over_text, (200, 250))


# game loop

while not exit_game:
    if snake_x < 5 or snake_x > (screen_width-5) or snake_y < 5 or snake_y > (screen_height-5):
        game_over = True
        game_over_text()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            elif event.type == pygame.KEYDOWN:
                if event.type == pygame.K_RETURN:


    else:
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


        snake_x += velocity_x
        snake_y += velocity_y


            # colision
        iscollision = collision(snake_x, snake_y, food_x, food_y)
        if iscollision:
            score_value += 10
            snake_length += 5
            #print("score:",score_value)
            food_x = random.randint(40, screen_width / 2)
            food_y = random.randint(20, screen_height / 2)

        gamewindow.fill(white)
        #pygame.draw.rect(gamewindow,black,[snake_x,snake_y,snake_size,snake_size])
        pygame.draw.rect(gamewindow, red, [food_x, food_y, food_size, food_size])
        head = []
        head.append(snake_x)
        head.append(snake_y)
        snake_list.append(head)
        if len(snake_list)>snake_length:
            del snake_list[0]

        plot_snake(gamewindow,black,snake_list,snake_size)
        show_score(textX, textY)
    pygame.display.update()
    clock.tick(fps)
pygame.quit()
quit()



