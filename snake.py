import pygame 
import random 

pygame.init()
pygame.font.init()



width , height = 600 , 400
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Hungry Snake 🐍")

white = (255 , 255 , 255)
black = (0 , 0 , 0)
green = (0 , 255 , 0)
red = (255 , 0 , 0)

snake_size = 10
snake_speed = 10 
clock = pygame.time.Clock()

font = pygame.font.SysFont(None,30)

def score_display(score):
    text = font.render("Score : " + str(score), True , black)
    screen.blit(text , [0,0])

def game_loop():
    game_over = False
    x = width/2
    y = height/2
    dx = 0 
    dy = 0 
    snake = []
    snake_length = 1
    food_x = round(random.randrange(0 , width - snake_size)/10) * 10
    food_y = round(random.randrange(0 , height - snake_size)/10) * 10
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -snake_size
                    dy = 0 
                elif event.key == pygame.K_RIGHT:
                    dx = snake_size
                    dy = 0
                elif event.key == pygame.K_UP:
                    dx = 0 
                    dy = - snake_size
                elif event.key == pygame.K_DOWN:
                    dx = 0 
                    dy = snake_size

        if x < 0 or x >= width or y < 0 or y >= height:
            game_over = True

        x += dx 
        y += dy 
        screen.fill(white) 

        pygame.draw.rect(screen , red, [food_x, food_y, snake_size, snake_size])
        snake.append([x, y])
        if len(snake) > snake_length:
            del snake[0]
        for block in snake[:-1]:
            if block == [x,y]:
                game_over = True

        for block in snake:
            pygame.draw.rect(screen , green , [block[0], block[1] , snake_size , snake_size])
        score_display(snake_length - 1)
        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0 , width - snake_size)/10) * 10
            food_y = round(random.randrange(0 , height - snake_size)/10) * 10
            snake_length += 1 
        
        clock.tick(snake_speed)
    pygame.quit()

game_loop()
