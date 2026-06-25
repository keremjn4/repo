import pygame
import random
import math

pygame.init()

TILE_SIZE = 20 



screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("square")

COL = 800 // TILE_SIZE
ROW = 600 // TILE_SIZE

def pixeltotile(x):
    return x//TILE_SIZE

def tiletopixel(t):
    return t*TILE_SIZE

def tilesize(size):
    return size*TILE_SIZE

def drawtile(color, row, col, size=1, obstacle = False):
    pygame.draw.rect(screen, color, (col*TILE_SIZE + 1/2*(TILE_SIZE - TILE_SIZE/size), row*TILE_SIZE + 1/2*(TILE_SIZE - TILE_SIZE/size), TILE_SIZE/size, TILE_SIZE/size))

            
font = pygame.font.SysFont(None, 18)
foodw = 3
foodh = 3

wall = pygame.Rect(400, 0,5, 550)

initialposx = random.randint(0,800-foodw)
initialposy = random.randint(0,600-foodh)

foodimg = pygame.Rect(initialposx, initialposy, foodw, foodh)

SEEK_FOOD = "SEEK_FOOD"
SEEK_GAP = "SEEK_GAP"
EXIT_GAP = "EXIT_GAP"

class SQUARE:
 def __init__(self, col, row, size):
     self.rect = pygame.Rect(tiletopixel(col),tiletopixel(row),tiletopixel(size),tiletopixel(size))
     self.mode = None
     self.col = col
     self.row = row
     self.size = size

 def move(self, dx = 0 ,dy = 0):  
            self.col += dx
            self.row += dy  
            self.rect.x = tiletopixel(self.col)
            self.rect.y = tiletopixel(self.row)

                    
 def change_mode(self,new_mode):
     if new_mode != self.mode:
         self.mode = new_mode
         print(f'mode: {new_mode}')
        
gap = pygame.Rect(wall.x, wall.height, wall.width, 600-wall.height)

while foodimg.colliderect(wall):
    foodimg.x = random.randint(0, 800 - foodw)
    foodimg.y = random.randint(0, 600 - foodh)

food = foodimg

score = 0

clock = pygame.time.Clock()

running = True

ai_mode = False

square = SQUARE(6,8,0.5)

wall = []
tile = []

while running:
    clock.tick(30)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
               running = False   
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                ai_mode = not ai_mode
                print(f'AI: {ai_mode}')


    if ai_mode == False:
        dx=1
        dy=1
        ai_text = font.render(f'AI: {ai_mode}', True , (255,0,0))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            if (square.row+dx,square.col+dx) in tile:
                square.move(dx,0)
        if keys[pygame.K_LEFT]:
            if (square.row-dx,square.col-dx) in tile:
                square.move(-dx,0)        
        if keys[pygame.K_DOWN]:
            if (square.row+dx,square.col+dx) in tile:
                square.move(0,dy)        
        if keys[pygame.K_UP]:
            if (square.row-dx,square.col-dx) in tile:
                square.move(0,-dy)                
            
    if ai_mode:
        ai_text = font.render(f'AI: {ai_mode}', True , (0,255,0))       

                      
    screen.fill((0,0,0))

    if square.rect.colliderect(food):
        score +=1
        food.x = random.randint(0,800-foodw)
        food.y = random.randint(0,600-foodh)

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
   
    screen.blit(score_text, (10, 10))
    screen.blit(ai_text, (10,30))

    tile.clear()
    wall.clear()

    for c in range (0,COL):
        for r in range (0,ROW):
         drawtile((0,0,0), r,c)
         tile.append((r,c))    
    

    for x in range (0,14):
     drawtile((0,0,255), x, 19)
     wall.append((x,19))
     drawtile((0,0,255), x, 20)
     wall.append((x,20))
 

    for x in range (16,30):
     drawtile((0,0,255), x, 19)
     wall.append((x,19))
     drawtile((0,0,255), x, 20)
     wall.append((x,20))

    for x in range(0, 800, TILE_SIZE):
        pygame.draw.line(screen, (50,50,50), (x,0), (x,600))

    for y in range(0, 600, TILE_SIZE):
        pygame.draw.line(screen, (50,50,50), (0,y), (800,y))

    pygame.draw.rect(screen,(0,255,0), food)

    pygame.draw.rect(screen,(255,255,255), square.rect)
    print(len(tile))


    drawtile((0,255,255),10,10,2)

    pygame.display.flip()

pygame.quit()

