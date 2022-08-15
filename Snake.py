import time
import pygame
import random
pygame.init()


white = (255, 255, 255)
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis=pygame.display.set_mode((800,600))
pygame.display.set_caption('Snake')

game_over=False

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 
def message(msg,color,x,y):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [x,y])
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
x1=300
y1=400
x1_change=0
y1_change=0

clock=pygame.time.Clock()

def gameLoop():
    count=0
    diffs=10
    score=0
    game_over = False
    game_close = False
    x1 = 400
    y1 = 300
 
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, 800 - 10) / 10.0) * 10.0
    foody = round(random.randrange(0, 600 - 10) / 10.0) * 10.0
    while not game_over:
      
      
      while game_close == True:
                dis.fill(white)
                message("You Lost!", red,300,300)
                message("Q:Quit game",black,300,325)
                message("R:Retry",black,300,350)
                pygame.display.update()
    
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_r:
                            gameLoop()

      for event in pygame.event.get():
        if event.type==pygame.QUIT:
          game_over=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
              x1_change=-10
              y1_change=0
              
            if event.key==pygame.K_RIGHT:
              x1_change=10
              y1_change=0
              
            if event.key==pygame.K_UP:
              x1_change=0
              y1_change=-10
              
            if event.key==pygame.K_DOWN:
              x1_change=0
              y1_change=10
              
        
      if not x1 in range(0,800) or not y1 in range(0,600):
        game_close=True  
      
      x1+=x1_change
      y1+=y1_change
      dis.fill(white)

      pygame.draw.rect(dis, green, [foodx, foody, 10, 10])
      snake_Head = []
      snake_Head.append(x1)
      snake_Head.append(y1)
      snake_List.append(snake_Head)
      if len(snake_List) > Length_of_snake:
            del snake_List[0]

      for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
      
      our_snake(10, snake_List)
      
      pygame.draw.rect(dis, blue, [foodx, foody, 10, 10])
      pygame.draw.rect(dis, black, [x1, y1, 10, 10])
      pygame.display.update()
      
      pygame.draw.rect(dis, black, [x1, y1, 10, 10])
      pygame.display.update()
      if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, 800 - 10) / 10.0) * 10.0
                foody = round(random.randrange(0, 600 - 10) / 10.0) * 10.0
                Length_of_snake += 1
                count+=1
                diffs+=0.7
                score+=int(1000*(diffs+Length_of_snake*0.5+random.randrange(0,10000000)/10000000))
      message("Score:"+str(score), blue,0,0)
      pygame.display.update()
      clock.tick(int(diffs))
    pygame.display.update()
    pygame.quit()
    quit()

gameLoop()