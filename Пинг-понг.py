from pygame import *
clock = time.Clock()
main = display.set_mode((700, 500))
display.set_caption('Пинг-Понг')
class Game_Sprite(sprite.Sprite):
    def __init__(self, name_picture, speed, x1, y1, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(name_picture), (size_x, size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x1
        self.rect.y = y1
    def blit1(self):
        main.blit(self.image, (self.rect.x, self.rect.y))
class Player(sprite.Sprite):
    def __init__(self, color_fill, speed, x1, y1, size_x, size_y):       
        self.image = Surface((size_x, size_y))
        self.image.fill((color_fill[0], color_fill[1], color_fill[2]))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x1
        self.rect.y = y1
    def blit1(self):
        main.blit(self.image, (self.rect.x, self.rect.y))
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] == True and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] == True and self.rect.y < 400:
            self.rect.y += self.speed
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_o] == True and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_l] == True and self.rect.y < 400:
            self.rect.y += self.speed
class Ball(Game_Sprite):
    def __init__(self, name_picture, speed, x1, y1, size_x, size_y, speed_x, speed_y):       
        Game_Sprite.__init__(self, name_picture, speed, x1, y1, size_x, size_y)
        self.speed_x = speed_x
        self.speed_y = speed_y
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        global flag2
        if self.rect.y >= 450 or self.rect.y <= 0:
            self.speed_y *= -1
        if self.rect.x <= 0:
            flag2 = False
            main.blit(font2, (250, 210))
        if self.rect.x >= 650:
            flag2 = False
            main.blit(font3, (250, 210))
font.init()
font1 = font.SysFont('Arial', 40)
font2 = font1.render('Player №1 проиграл!... :)', True, (255, 255, 255))
font3 = font1.render('Player №2 проиграл!... :)', True, (0, 0, 0))
rocket1 = Player([255, 255, 255], 3, 10, 200, 20, 100)
rocket2 = Player([0, 0, 0], 3, 670, 200, 20, 100)
ball = Ball('pngegg.png', 5, 325, 225, 50, 50, 4, 4)
flag = True
flag2 = True
while flag != False:
    if flag2 == True:
        main.fill((107, 142, 35))
        ball.update()
        if sprite.collide_rect(ball, rocket2):
            ball.speed_x *= -1
        if sprite.collide_rect(ball, rocket1):
            ball.speed_x *= -1

        ball.blit1()
        rocket1.update_left()
        rocket1.blit1()
        rocket2.update_right()
        rocket2.blit1()


    for ev in event.get():
        if ev.type == QUIT:
            flag = False
    clock.tick(60)
    display.update()




