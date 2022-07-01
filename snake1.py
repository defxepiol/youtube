import pygame
import random, math

WIDTH=500
HEIGHT=500
side_screen_size = 200

size = 20 #size of snake, food, grid
FPS = 16

black = (0,0,0)
white = (255,255,255)
gray = (25,25,25)
yellow = (255,255,0)
blue = (0,100,255)
red = (255,0,0)
green = (0,255,0)
pink = (238,127,255)
purple = (100,0,255)
orange = (255,143,0)

mycolors=[white,yellow,blue,green,pink,purple,orange]

pygame.init()
window = pygame.display.set_mode((WIDTH+1+side_screen_size,HEIGHT+1))
pygame.display.set_caption("Skane")
clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.length = length+1
        self.head_x = [size]*self.length
        self.head_y = [size]*self.length
        self.color = mycolors[random.randint(0,len(mycolors)-1)]

    def move(self): 
        global points, head_colliding
        if not head_colliding:
            if up:
                self.head_y[0] -= size
            if down:
                self.head_y[0] += size
            if left:
                self.head_x[0] -= size
            if right:
                self.head_x[0] += size
        
            for i in range(1,self.length): 
                if self.head_x[0] == self.head_x[i] and self.head_y[0] == self.head_y[i]:
                    head_colliding = True

            if self.head_x[0] == food.pos_food_x and self.head_y[0] == food.pos_food_y:
                itIs=True
                while itIs: 
                    r1=random.randint(0,int(WIDTH/size)-1)
                    r2=random.randint(0,int(WIDTH/size)-1)
                    itIs=False
                    for i in range(self.length):
                        if r1*size == self.head_x[i] and r2*size == self.head_y[i]:
                            itIs= True
                              
                if itIs == False:
                    food.pos_food_x = r1*size 
                    food.pos_food_y = r2*size
  
                points+=1
                self.length+=1
                self.head_x.append(size)
                self.head_y.append(size)

            for i in range(self.length-1,0,-1):
                self.head_x[i] = self.head_x[i-1]
                self.head_y[i] = self.head_y[i-1]    
            
    def draw(self):
        for i in range(self.length):
            
            if self.head_y[i] > HEIGHT-size:
                self.head_y[i] = 0
            elif self.head_y[i] < 0:
                self.head_y[i] = HEIGHT-size
            elif self.head_x[i] < 0:
                self.head_x[i] = WIDTH-size
            elif self.head_x[i] > WIDTH-size:
                self.head_x[i] = 0
            
            pygame.draw.rect(window,self.color,(self.head_x[i],self.head_y[i],size,size))

class Food:
    def __init__(self):
        r = random.randint(0,24)
        self.pos_food_x = r*size
        self.pos_food_y = r*size
  
    def draw(self):
        pygame.draw.rect(window,red,(self.pos_food_x,self.pos_food_y,size,size))

def grid():
    for i in range(int(WIDTH/size)+1):
        pygame.draw.line(window,(gray),(i*size,0),(i*size,HEIGHT))
    for j in range(int(HEIGHT/size)+1):
        pygame.draw.line(window,(gray),(0,j*size),(WIDTH,j*size))
    
def textpoints():
    font = pygame.font.Font("freesansbold.ttf",20)
    text = font.render("Score: "+str(points),True,(255,255,255),(0,0,0))
    window.blit(text, (WIDTH+side_screen_size/4 + 10, HEIGHT/2 - 100))

    if head_colliding:
        text = font.render("Bye Bye :(",True,(255,255,255),(0,0,0))
        window.blit(text, (WIDTH+side_screen_size/4, HEIGHT/2))

        pygame.draw.rect(window,(140,56,56),(snake.head_x[0],snake.head_y[0],size,size))
      

def movement():
    global right, left, down, up
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_UP] and down == False:
        right = False
        left = False
        down = False
        up = True
    elif keys_pressed[pygame.K_DOWN] and up == False:
        right = False
        left = False
        up = False
        down = True
    elif keys_pressed[pygame.K_LEFT] and right == False:
        right = False
        down = False
        up = False
        left = True
    elif keys_pressed[pygame.K_RIGHT] and left == False:
        left = False
        down = False
        up = False
        right = True

points = 0
length = 1  
snake=Snake()
food = Food()

right = True
left = False
up = False
down = False

head_colliding = False

run = True
while run:
    window.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    movement()
    snake.move()
    snake.draw()
    food.draw()
    textpoints()
    grid()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()